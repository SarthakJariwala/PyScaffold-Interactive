import nox

nox.options.sessions = "tests"


@nox.session
def tests(session):
    """Run tests"""
    session.install("-e", ".", "pytest", "pytest-cov")
    session.run("pytest")


@nox.session
def black(session):
    """Run black code formatter"""
    session.install("black", "isort")
    files = ["src", "tests", "noxfile.py"]
    session.run("black", *files)
    session.run("isort", "--recursive", *files)
