import pytest



@pytest.fixture(scope="module")

def test_fixture1():
    print("This is first fixture setup")


@pytest.fixture(scope="function")
def test_fixture2():
    print("This is second fixture setup")
    yield
    print("This is fixture setup after yield")

def test_1(test_fixture1,test_fixture2):
    print("This is first test")

def test_2():
    print("This is second test")

