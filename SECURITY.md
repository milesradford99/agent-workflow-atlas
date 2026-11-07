# Security and privacy

This repository is mostly documentation. Two kinds of problem should still be reported privately rather than in a public issue:

- **Something that shouldn't be here:** a secret, credential or token; personal data such as names, emails, patient, student or candidate details; or material shared without the right to do so. This applies especially to the context files and samples in `examples/` folders.
- **A vulnerability in the code** under `scripts/` or `.github/`, for example a way for a pull request to run code with the repository's permissions.

## How to report

Use GitHub's private reporting: the **Security** tab → **Report a vulnerability**. Include the file path and commit if you can. Please don't open a public issue or pull request that contains the material itself.

Expect a first reply within a week. This is a volunteer project and there is no bounty. Material that shouldn't be here is removed from the current files at once. If it needs removing from history too, we rewrite history and tell you when it's done. Leaked credentials should be revoked at their source, since removing them from the repository doesn't make them safe again.

Ordinary mistakes in a workflow, like a wrong number, a dead link or an outdated tool, aren't security issues. Use the [correction form](.github/ISSUE_TEMPLATE/correction.yml) for those.
