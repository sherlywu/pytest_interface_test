import pytest

# 所有用例运行之前执行的代码
@pytest.fixture(scope='session', autouse=True)
def session():
    print('before all testcases')
    yield
    print('after all testecase')

@pytest.fixture(scope='function', autouse=True)
def case():
    print('testcase 运行之前')
    yield
    print('testcase 运行之后')

@pytest.fixture(scope='class', autouse=True)
def classcase():
    print('class运行之前')
    yield
    print('class运行之后')

@pytest.fixture(scope='module', autouse=True)
def module():
    print('module 运行之前')
    yield
    print('module 运行之后')


def test_01():
    print('test01')
    assert True

def test_02():
    print('test02')
    assert True

def test_03():
    print('test03')
    assert True
