# Poetry PDF

Poetry formatter to PDF.

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install poetry-pdf
```

## Usage

Plaintext is converted into html and pdfkit is used to export a PDF.

Exposed CLI:

```bash
poetry-pdf <source_path>
            [--output-dir=<output_dir>]
            [--author=<author>]
            [--stylesheet=<stylesheet>]...
```

Example invocation:

```bash
poetry-pdf "the_raven.txt" --output-path "." --author "Edgar Allan Poe"
```

Intermediate html:

```html
<head>
  <meta charset="utf-8" />
  <link
    rel="stylesheet"
    type="text/css"
    href="/Users/joel/Workspace/poetry-pdf/poetry_pdf/styles/default.css"
  />
</head>
<body>
  <h1 id="title">The Raven</h1>
  <br />
  <p id="poem">
    Once upon a midnight dreary, while I pondered, weak and weary,<br />
    Over many a quaint and curious volume of forgotten lore—<br />
    While I nodded, nearly napping, suddenly there came a tapping,<br />
    As of some one gently rapping, rapping at my chamber door.<br />
    “’Tis some visitor,” I muttered, “tapping at my chamber door—<br />
    Only this and nothing more.”<br />
    <br />
    Ah, distinctly I remember it was in the bleak December;<br />
    And each separate dying ember wrought its ghost upon the floor.<br />
    Eagerly I wished the morrow;—vainly I had sought to borrow<br />
    From my books surcease of sorrow—sorrow for the lost Lenore—<br />
    For the rare and radiant maiden whom the angels name Lenore—<br />
    Nameless here for evermore.<br />
  </p>
  <br />
  <p id="author">Edgar Allan Poe</p>
</body>
```

Generated pdf:

![raven][raven]

Custom stylesheets can be specified:

```bash
poetry-pdf "the_raven.txt" --stylesheet "./sheet1.css" --stylesheet "./sheet2.css"
```

If no stylesheets are provided the page styles will default to:

```css
body {
  font-family: "Avenir Next", sans-serif;
  margin: 100px;
}

#title {
  font-size: 70px;
  font-weight: 500;
  text-align: center;
}

#poem,
#author {
  font-style: italic;
  font-weight: 400;
  font-size: 20px;
  line-height: 35px;
}

#author {
  text-align: right;
}
```

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
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

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

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

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/poetry-pdf/pulls
[issues]: https://github.com/JoelLefkowitz/poetry-pdf/issues
[raven]: https://github.com/JoelLefkowitz/poetry-pdf/blob/master/example.jpg?raw=true

<!-- External links -->

[readthedocs]: https://poetry-pdf.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/poetry-pdf
[license_shield]: https://img.shields.io/github/license/joellefkowitz/poetry-pdf
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/poetry-pdf

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/poetry-pdf
[codacy_shield]: https://img.shields.io/codacy/coverage/poetry-pdf
[coverage_shield]: https://img.shields.io/codacy/grade/poetry-pdf
[readthedocs_shield]: https://img.shields.io/readthedocs/poetry-pdf

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/poetry-pdf
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/poetry-pdf

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/poetry-pdf
[python_versions_shield]: https://img.shields.io/pypi/pyversions/poetry-pdf
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/poetry-pdf

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/poetry-pdf
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/poetry-pdf
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/poetry-pdf
