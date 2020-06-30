# -*- coding: utf-8 -*-

import pytest
import click
from click.testing import CliRunner
import sys
sys.path.append("src/")
from pyscaffold_interactive import cli as pysci #import main, prompt_text, prompt_choice

__author__ = "Sarthak Jariwala"
__copyright__ = "Sarthak Jariwala"
__license__ = "mit"


def test_default_vs_input():
    """Test if the default value provided is overwritten by user input"""
    
    @click.command()
    def cli():
        ans = pysci.prompt_text("Project name", default="PyProject")
        click.echo(f'Project Name = {ans}')

    runner = CliRunner()
    result = runner.invoke(cli, input="My Python Project\n")
    assert not result.exception
    assert result.output == "Project name [PyProject]: My Python Project\nProject Name = My Python Project\n"

def test_choices():
    """Test if an error is thrown when user provides an input that is not in choices"""

    @click.command()
    def cli():
        ans = pysci.prompt_choice("Confrim", ['y', 'n'], default='y')
    
    runner = CliRunner()
    result = runner.invoke(cli, input='z')

    assert result.output != 'y' # check if the output is not equal to default

def test_choice_iterable():
    """Test if choices are iterable"""
    
    with pytest.raises(AssertionError):
        pysci.prompt_choice("Confrim", 1)

def test_main():
    """Test interactive creation of pyscaffold"""

    @click.command()
    def cli():
        pysci.main()

    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0

