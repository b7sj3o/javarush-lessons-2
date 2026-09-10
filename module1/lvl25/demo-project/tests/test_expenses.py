import pytest

from expenses import average, by_category, top_category, total


@pytest.fixture
def sample() -> list[dict]:
    return [
        {"title": "Coffee", "amount": 85.0, "category": "food"},
        {"title": "Transit pass", "amount": 500.0, "category": "transport"},
        {"title": "Lunch", "amount": 240.0, "category": "food"},
    ]


def test_total(sample):
    assert total(sample) == 825.0


def test_total_empty():
    assert total([]) == 0


def test_by_category(sample):
    assert by_category(sample) == {"food": 325.0, "transport": 500.0}


def test_average(sample):
    assert average(sample) == pytest.approx(275.0)


def test_average_empty_does_not_crash():
    """The edge case a reviewer always asks about."""
    assert average([]) == 0.0


def test_top_category(sample):
    assert top_category(sample) == "transport"


def test_top_category_empty():
    assert top_category([]) is None
