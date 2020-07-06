import nox


@nox.session
def tests(session):
    """Run tests"""
    session.install("-e", ".", "pytest", "pytest-cov")
    session.run("pytest")


@nox.session
def blacken(session):
    """Run black code formatter"""
    session.install("black==19.3b0", "isort==4.3.21")
    files = ["src", "tests", "noxfile.py", "setup.py"]
    session.run("black", *files)
    session.run("isort", "--recursive", *files)
