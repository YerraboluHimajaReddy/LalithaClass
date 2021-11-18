import sys

import pytest


@pytest.mark.skip
def test_login():
    print("login done")

@pytest.mark.skipif(sys.version_info<(3,8), reason="python version is not supporting")
def test_name():
    print("name is Himaja")

@pytest.mark.skipif(sys.version_info<(3,5), reason="python version is not supporting")
def test_nameA():
    print("name is Himaja")

@pytest.mark.xfail
def test_product():
    assert False
    print("Product done")

@pytest.mark.xfail
def test_product1():
    assert True
    print("Product done")

# platform win32 -- Python 3.5.1, pytest-6.1.2, py-1.11.0, pluggy-0.13.1
# rootdir: C:\Users\Sony\PycharmProjects\LalithaClass\LalithaPythonClass\PYTest_Framework, configfile: pytest.ini
# plugins: html-1.22.1, metadata-1.8.0
# collected 5 items
#
# PYtest_Markers2.py ss.xX                                                                                                   [100%]
#
# ====================================== 1 passed, 2 skipped, 1 xfailed, 1 xpassed i

