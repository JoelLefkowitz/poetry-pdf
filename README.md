# Poetry PDF

Poetry formatter

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

<!--- Table links --->

[license]: https://img.shields.io/github/license/JoelLefkowitz/poetry-pdf

[release]: https://img.shields.io/github/v/tag/JoelLefkowitz/poetry-pdf

[pypi_downloads]: https://img.shields.io/pypi/dw/poetry_pdf

[pypi]: https://img.shields.io/pypi/v/poetry_pdf "PyPi"

[pypi_link]: https://pypi.org/project/poetry_pdf

[issues]: https://img.shields.io/github/issues/JoelLefkowitz/poetry-pdf "Issues"

[issues_link]: https://github.com/JoelLefkowitz/poetry-pdf/issues

[pulls]: https://img.shields.io/github/issues-pr/JoelLefkowitz/poetry-pdf "Pull requests"

[pulls_link]: https://github.com/JoelLefkowitz/poetry-pdf/pulls

### Usage

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
  <h1 id="title">
    The Raven
  </h1>
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
  <p id="author">
    Edgar Allan Poe
  </p>
</body>
```

Generated pdf:

![the_raven.pdf](https://github.com/JoelLefkowitz/poetry-pdf/blob/master/example.jpg?raw=true)

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

#poem, #author {
    font-style: italic;
    font-weight: 400;
    font-size: 20px;
    line-height: 35px;
  }

#author {
    text-align: right;
  }
```

### Installing

To install the package from pypi:

```bash
pip install poetry_pdf
```

Alternatively, you can clone the repo and build the package locally.

### Docs

Additional details are available in the [full documentation](https://poetry-pdf.readthedocs.io/en/latest/).

To generate the documentation locally:

```bash
multi-job docs
```

### Tests

Unit tests and behaviour tests are written with the pytest framework.

To run tests:

```bash
multi-job tests
```

Additionally, an html report will be saved to the local directory.

### Buildbot

To run the buildbot server:

```bash
cd ci
docker-compose up -d
```

-   Builders are configured in master.cfg.
-   Build masters read their configuration from <https://github.com/JoelLefkowitz/poetry-pdf/poetry_pdf/ci/master.cfg>
-   Worker and database passwords are configured as environment variables

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

### Versioning

[SemVer](http://semver.org/) is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.

### Author

-   **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!
