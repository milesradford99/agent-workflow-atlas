"""Regression checks for move metadata, translation and public outputs."""
import copy
import csv
import io
import tempfile
import unittest
from pathlib import Path

import yaml

import build_index
import build_site
import i18n
import site_pages
from catalog import ROOT, load_taxonomy, read_front_matter, species_files
from validate import check_species


class MovesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tax = load_taxonomy()
        cls.path = next(p for p in species_files() if read_front_matter(p)[0]['id'] == 'AWF-0001')
        cls.fm, _ = read_front_matter(cls.path)
        cls.workflows = build_site.records(cls.tax)
        cls.data = {'repo': 'https://github.com/example/atlas',
                    'labels': yaml.safe_load((ROOT / 'i18n/labels.yaml').read_text())}

    def errors(self, **updates):
        fm = dict(copy.deepcopy(self.fm), **updates)
        errs = []
        check_species(self.path, fm, self.tax, errs)
        return '\n'.join(errs)

    def test_moves_are_required_and_malformed_values_are_rejected(self):
        fm = dict(self.fm)
        del fm['move']
        errs = []
        check_species(self.path, fm, self.tax, errs)
        self.assertTrue(any('missing field(s): move' in e for e in errs))
        for moves, move, expected in [
            (['verify', 'verify'], 'Check the result.', 'must not repeat'),
            (['standard', 'verify'], 'Check the result.', 'cannot be combined'),
            (['unknown'], 'Check the result.', 'not one of'),
            ('verify', 'Check the result.', 'list of one or two'),
            (['verify'], 42, '300 characters'),
            (['verify'], 'x' * 301, '300 characters'),
        ]:
            with self.subTest(moves=moves, move=move):
                self.assertIn(expected, self.errors(moves=moves, move=move))

    def test_translation_catches_changed_move_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme = Path(tmp) / 'README.md'
            readme.write_text(self.path.read_text())
            zh = readme.with_name(i18n.ZH_NAME)
            original = self.path.with_name(i18n.ZH_NAME).read_text()
            text = original
            text = text.replace('\nmove:', '\nold_move:', 1)
            text = text.replace('\nsource_hash:', '\nmove: "核实 41% 的输出。"\nsource_hash:', 1)
            zh.write_text(text)
            fm = dict(self.fm, move='Verify 42% of outputs.')
            errs, _ = i18n.problems(readme, fm)
            self.assertTrue(any('keep the English numbers' in e for e in errs))
            zh.write_text(text.replace('41%', '42%'))
            errs, _ = i18n.problems(readme, fm)
            self.assertFalse(any('keep the English numbers' in e for e in errs))

    def test_bilingual_move_reaches_page_app_json_and_csv(self):
        w = next(w for w in self.workflows if w['id'] == 'AWF-0001')
        self.assertNotEqual(w['move'], w['moveZh'])
        for lang, sentence in [('en', w['move']), ('zh-CN', w['moveZh'])]:
            page = site_pages.page(w, self.data, '', '', lang)
            self.assertIn('<p class="move">' + site_pages.esc(sentence) + '</p>', page)
            self.assertLess(page.index('class="move"'), page.index('class="lede"'))
        app = build_site.app_record(w, self.data['repo'])
        self.assertEqual(app['moves'], w['moves'])
        self.assertEqual(app['moveZh'], w['moveZh'])
        rows = site_pages.export_rows([w], self.data['repo'], '')
        row = next(csv.DictReader(io.StringIO(site_pages.to_csv(rows))))
        self.assertEqual(row['moveZh'], w['moveZh'])
        self.assertEqual(row['moves'], '; '.join(w['moves']))

    def test_archived_links_keep_bilingual_status_and_canonical_target(self):
        w = next(w for w in self.workflows if w['id'] == 'AWF-0222')
        for lang, target in [('en', '../../w/AWF-0110/'), ('zh-CN', '../../../w/AWF-0110/zh/')]:
            page = site_pages.page(w, self.data, '', '', lang)
            self.assertIn('class="note status-note"', page)
            self.assertIn('href="' + target + '"', page)
        retired = next(w for w in self.workflows if w['status'] == 'retired')
        self.assertIn(site_pages.UI['zh-CN']['retired'], site_pages.page(retired, self.data, '', '', 'zh-CN'))

    def test_index_groups_active_entries_by_move_before_field(self):
        rendered = build_index.render(build_index.load(), self.tax)
        self.assertLess(rendered.index('## By move'), rendered.index('## By field'))
        by_move = rendered.split('## By move', 1)[1].split('## By field', 1)[0]
        self.assertIn('AWF-0001', by_move)
        self.assertNotIn('AWF-0222', by_move)
        self.assertNotIn('AWF-0013', by_move)


if __name__ == '__main__':
    unittest.main()
