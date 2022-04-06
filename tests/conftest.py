# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for pyscaffold_interactive.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest

import subprocess


@pytest.fixture()
def delete_folder_after_test():
    yield
    subprocess.run(["rm", "-rf", "PyProject"])
