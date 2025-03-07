import pytest

from source.accum import Accumulator


@pytest.fixture
def accum_global():
    return Accumulator()
