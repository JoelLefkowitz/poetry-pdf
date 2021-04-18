module.exports = function (grunt) {
  grunt.initConfig({
    exec: {
      bandit: "bandit --ini .bandit -r poetry_pdf",
      black: "black poetry_pdf",
      cspell: "npx cspell -c .cspell.json {*,.*,**/*}",
      isort: "isort poetry_pdf",
      mypy: "mypy poetry_pdf",
      prettier: "prettier . --write",
      pylint: "pylint --rcfile .pylintrc  --fail-under=8 poetry_pdf",
      quickdocs: "quickdocs .quickdocs.yml",
      remark: "npx remark -r .remarkrc .",
      sphinx: "sphinx-build docs build",
      tox: "tox",
    },
  });

  grunt.loadNpmTasks("grunt-exec");

  grunt.registerTask(
    "lint",
    "Lint the source code",
    ["cspell", "remark", "pylint", "bandit", "mypy"].map((i) =>
      "exec:".concat(i)
    )
  );

  grunt.registerTask(
    "format",
    "Format the source code",
    ["prettier", "black", "isort"].map((i) => "exec:".concat(i))
  );

  grunt.registerTask("tests:unit", "Run unit tests", "exec:tox");

  grunt.registerTask(
    "docs:generate",
    "Generate a Sphinx documentation configuration",
    "exec:quickdocs"
  );

  grunt.registerTask(
    "docs:build",
    "Build documentation from a Sphinx configuration",
    "exec:sphinx"
  );

  grunt.registerTask(
    "precommit",
    "Run a sequence of precommit quality control tasks",
    ["lint", "tests:unit", "docs:generate"]
  );
};
