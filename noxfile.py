import nox

nox.options.sessions = ("tests",)


@nox.session
def tests(session):
    """Run tests"""
    session.install("-e", ".", "pytest", "pytest-cov", "coverage[toml]")
    session.run("pytest")


@nox.session
def black(session):
    """Run black code formatter"""
    session.install("black", "isort")
    files = ["src", "tests", "noxfile.py"]
    session.run("black", *files)
    session.run("isort", "--recursive", *files)


@nox.session
def coverage(session):
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml")
    session.run("codecov", *session.posargs)
