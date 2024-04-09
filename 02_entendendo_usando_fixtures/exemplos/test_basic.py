import pytest


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


def test_list(sample_data):
    assert sample_data == [1, 2, 3, 4, 5]


def test_sum(sample_data):
    assert sum(sample_data) == 15


def test_len(sample_data):
    assert len(sample_data) == 5
