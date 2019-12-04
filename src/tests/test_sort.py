from sorts import Sort
import pytest
import random


@pytest.fixture(scope='module', autouse=True)
def start_up():
    print('hello world')

@pytest.fixture(scope='module')
def init_data():
    return [random.randint(0, 1000) for _ in range(100)]

def test_sort(init_data):
    data = init_data
    data_test = data[:]
    data_test.sort()
    sort_data = Sort.RandomQuicksort(data)
    assert sort_data == data_test

def test_quick(init_data):
    data = init_data
    data_test = data[:]
    data_test.sort()
    sort_data = Sort.Quicksort(data)
    assert sort_data == data_test

@pytest.mark.parametrize('n, res', [(0, 0),
                                    (1, 1),
                                    (2, 1),
                                    (3, 2),
                                    (4, 3),
                                    (5, 5),
                                    (6, 8)])
def test_fibonacci(n, res):
    assert Sort.fibonacci(n) == res

if __name__ == '__main__':
    pytest.main(["-s", "-v"])
