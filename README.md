# Poetry PDF

Poetry formatter to PDF.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/poetry-pdf/review.yml)
![Version](https://img.shields.io/pypi/v/poetry-pdf)
![Downloads](https://img.shields.io/pypi/dw/poetry-pdf)
![Quality](https://img.shields.io/codacy/grade/1072e5a889e24a299039fc8978480181)
![Coverage](https://img.shields.io/codacy/coverage/1072e5a889e24a299039fc8978480181)

## Installing

```bash
pip install poetry-pdf
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/poetry-pdf).

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

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
