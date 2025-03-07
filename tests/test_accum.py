from source.accum import Accumulator
import pytest
import math


@pytest.fixture
def accum():
    return Accumulator()


def test_new_accum(accum_global,accum):
    assert accum.count == 0
    assert accum_global.count == 0


def test_add_counts(accum):
    accum.add_counts()
    assert accum.count == 1


def test_add_twice(accum):
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2


def test_add_with_paramas(accum):
    accum.add_counts(10)
    assert accum.count == 10


def test_add_counts_and_setter(accum):
    accum.count = 2
    accum.add_counts()
    assert accum.count == 3


def test_get_brend(accum):
    with pytest.raises(AttributeError) as err:
        print(accum.__brand)
    assert str(err.value) == "'Accumulator' object has no attribute '__brand'"


def test_math():
    assert math.pow(3, 3) == 27
