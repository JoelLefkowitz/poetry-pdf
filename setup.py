from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["docopts", "jinja2", "pdfkit"],
        entry_points={
            "console_scripts": [
                "poetry-pdf = poetry_pdf.__main__:entrypoint"
            ]
        },
        extras_require={
            "tests": [
                "pytest-bdd",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-watch",
                "pytest",
                "tox",
            ],
            "tools": [
                "autoflake",
                "bandit",
                "black",
                "bump2version",
                "isort",
                "mypy",
                "pylint",
                "quickdocs",
                "twine",
                "wheel",
            ],
        },
    )
