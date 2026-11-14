"""Regression checks for the Markdown used in workflow pages.

Run with python -m unittest discover -s scripts -p 'test_*.py'.
"""
from html.parser import HTMLParser
import unittest

from site_pages import markdown


class TableRows(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.rows.append(0)
        elif tag in ("th", "td"):
            self.rows[-1] += 1

    def handle_data(self, data):
        self.text.append(data)


class WorkflowTablesTest(unittest.TestCase):
    def test_route_alternatives_stay_in_one_cell(self):
        table = """| Step | Built as |
|---|---|
| rule-covered: propose status \\| judgement call: review | Skill |
| `create \\| update \\| skip` | MCP server (connector) |
"""
        parsed = TableRows()
        parsed.feed(markdown(table, lambda url: url))
        self.assertEqual(parsed.rows, [2, 2, 2])
        self.assertIn("rule-covered: propose status | judgement call: review", parsed.text)
        self.assertIn("create | update | skip", parsed.text)

    def test_escaped_backslash_does_not_escape_column_boundary(self):
        parsed = TableRows()
        parsed.feed(markdown("| Step | Built as |\n|---|---|\n| path \\\\| Skill |", lambda url: url))
        self.assertEqual(parsed.rows, [2, 2])
        self.assertIn("path \\", parsed.text)


if __name__ == "__main__":
    unittest.main()
