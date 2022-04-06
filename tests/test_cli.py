# -*- coding: utf-8 -*-

import pytest

import click
from click.testing import CliRunner

from pyscaffold_interactive import cli as pysci

__author__ = "Sarthak Jariwala"
__copyright__ = "Sarthak Jariwala"
__license__ = "mit"


@pytest.fixture
def runner():
    return CliRunner()


def test_default_vs_input(runner):
    """Test if the default value provided is overwritten by user input"""

    @click.command()
    def cli():
        ans = pysci.prompt_text("Project name", default="PyProject")
        click.echo("Project Name = {}".format(ans))

    result = runner.invoke(cli, input="My Python Project\n")
    assert not result.exception
    assert (
        result.output
        == "Project name [PyProject]: My Python Project\nProject Name = My Python Project\n"
    )


def test_choices(runner):
    """Test if an error is thrown when user provides an input that is not in choices"""

    @click.command()
    def cli():
        pysci.prompt_choice("Confrim", ["y", "n"], default="y")

    result = runner.invoke(cli, input="z")

    assert result.output != "y"  # check if the output is not equal to default


def test_choice_iterable():
    """Test if choices are iterable"""

    with pytest.raises(AssertionError):
        pysci.prompt_choice("Confrim", 1)


@pytest.mark.usefixtures("delete_folder_after_test")
@pytest.mark.parametrize("ci", ["github", "gitlab", "None"])
@pytest.mark.parametrize("pre_commit", ["y", "n"])
@pytest.mark.parametrize("md_or_rst", ["md", "rst"])
def test_main(runner, delete_folder_after_test, ci, pre_commit, md_or_rst):
    """Test interactive creation of pyscaffold python project"""

    @click.command()
    def cli():
        return pysci.main()

    input = ""
    input += "PyProject\n"  # project name
    input += "My description\n"  # description
    input += "www.example.com\n"  # url
    input += "n\n"  # DS-porject? - yes/no
    input += f"{ci}\n"  # github-actions CI
    input += f"{pre_commit}\n"  # pre-commit
    input += f"{md_or_rst}\n"  # markdown text
    input += "mit\n"  # license

    result = runner.invoke(cli, input=input)
    assert not result.exception
    assert result.exit_code == 0


@pytest.mark.usefixtures("delete_folder_after_test")
@pytest.mark.parametrize("ci", ["github", "gitlab", "None"])
def test_main_dsproject(runner, delete_folder_after_test, ci):
    """Test interactive creation of pyscaffold datascience project"""

    @click.command()
    def cli():
        return pysci.main()

    input = ""
    input += "PyProject\n"  # project name
    input += "My description\n"  # description
    input += "www.example.com\n"  # url
    input += "y\n"  # DS-porject? - yes/no
    input += f"{ci}\n"  # github-actions CI
    input += "mit\n"  # license
    result = runner.invoke(cli, input=input)
    assert not result.exception
    assert result.exit_code == 0
