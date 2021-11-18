import pytest


@pytest.mark.smoke
def test_login():
    print("login done")

@pytest.mark.smoke
def test_name():
    print("name is Himaja")

@pytest.mark.regression
def test_product():
    print("Product done")

