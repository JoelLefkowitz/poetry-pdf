from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["docopts", "jinja2", "pdfkit"],
        console_scripts=["poetry_pdf = poetry_pdf.__main__:entrypoint"],
        extras_require={
            "dist": ["wheel", "twine", "bump2version"],
            "docs": [
                "sphinx",
                "pyimport",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "bs4" "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
