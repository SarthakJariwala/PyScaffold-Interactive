# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = pyscaffold_interactive.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

import click
from pyscaffold import templates, info
from pyscaffold.api import create_project
from pyscaffold.extensions.tox import Tox
from pyscaffold.extensions.travis import Travis

from pyscaffold_interactive import __version__

__author__ = "Sarthak Jariwala"
__copyright__ = "Sarthak Jariwala"
__license__ = "mit"

_logger = logging.getLogger(__name__)

license_choices = templates.licenses.keys()
extensions = []

def main():
  """Interactive Python project template setup
  """

  click.echo(
    click.style(f"\nPyScaffold-Interactive - A tool to interactively "+
    "create python project templates using PyScaffold\n", 
    fg="green")
  )

  project_name = click.prompt(
    click.style("Enter your project name ", fg="blue"),
    default="PyProject"
  )

  author = click.prompt(
    click.style("Package author name ", fg="blue"),
    default=info.username()
  )

  email = click.prompt(
    click.style("Author email", fg="blue"),
    default=info.email()
  )

  description = click.prompt(
    click.style("Enter your package description ", fg="blue"),
    default="Generated using PyScaffold and PyScaffold-Interactive"
  )

  license = click.prompt(
    click.style("Choose License\n", fg="blue"),
    show_choices=True,
    type=click.Choice(license_choices, case_sensitive=True),
    default='mit'
  )

  make_tox = click.prompt(
    click.style("Generate config files for automated testing using tox? ", fg='blue'),
    show_choices=True,
    type=click.Choice(['y','n'], case_sensitive=False),
    default='y'
  ).lower()

  if make_tox == 'y':
    extensions.append(Tox('tox'))

  create_travis = click.prompt(
    click.style("Generate config and script files for Travis CI.? ", fg='blue'),
    show_choices=True,
    type=click.Choice(['y','n'], case_sensitive=False),
    default='y'
  ).lower()

  if create_travis == 'y':
    extensions.append(Travis('travis'))

  create_project(
    project=project_name,
    license=license,
    extensions=extensions,
    opts={
      "description":f"{description}",
      "author":f"{author}",
      "email":f"{email}"
    }
  )

  click.echo(
    click.style(f"\nSuccess! {project_name} created. Lets code!", fg="green")
  )

  click.echo(
    click.style("\nAfter making changes you can update using - ", 
    fg="green") + 
    click.style(f"'putup {project_name} --update'", fg='red')
  )


def run():
    """Entry point for console_scripts
    """
    main()


if __name__ == "__main__":
    run()
