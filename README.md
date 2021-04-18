# Poetry PDF

Poetry formatter to PDF.

## Status

| Source     | Shields                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield]  ![lines][lines_shield] ![languages][languages_shield]                    |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![travis][travis_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]     |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                        |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]              |

## Installing

```bash
pip install poetry_pdf
```

## Usage

## Tests

To run unit tests and generate a coverage report:

```bash
grunt tests:unit
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before committing new code:

```bash
grunt precommit
```

This will run linters, formatters, tests, generate a test coverage report and the sphinx configuration.

## Continuous integration

This repository uses Travis CI to build and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->
[semver]: http://semver.org/

<!-- External links -->
[readthedocs]: https://poetry-pdf.readthedocs.io/en/latest/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->
[author]: https://github.com/joellefkowitz

<!-- Project shields -->
[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/poetry-pdf
[license_shield]: https://img.shields.io/github/license/joellefkowitz/poetry-pdf
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/poetry-pdf
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/poetry-pdf

<!-- Health shields -->
[codacy_shield]: https://img.shields.io/codacy/grade/1072e5a889e24a299039fc8978480181
[readthedocs_shield]: https://img.shields.io/readthedocs/poetry-pdf
[travis_shield]: https://img.shields.io/travis/com/joellefkowitz/poetry-pdf
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/1072e5a889e24a299039fc8978480181

<!-- Repository shields -->
[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/poetry-pdf
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/poetry-pdf
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/poetry-pdf
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/poetry-pdf

<!-- Publishers shields -->
[pypi_shield]: https://img.shields.io/pypi/v/poetry_pdf
[python_versions_shield]: https://img.shields.io/pypi/pyversions/poetry_pdf
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/poetry_pdf

<!-- Activity shields -->
[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/poetry-pdf
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/poetry-pdf
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/poetry-pdf
