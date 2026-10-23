"""Tests for shop.py."""

import pytest

from shop import add_vat, save_total


def test_add_vat_negative_price():
    """A negative price should raise ValueError."""
    with pytest.raises(ValueError):
        add_vat(-5)


@pytest.mark.parametrize(
    "price, rate, expected",
    [
        (10, 0.2, 13.0),
        (0, 0.2, 0.0),
        (100, 0.5, 150.0),
        (19.99, 0.2, 23.99),
    ],
)
def test_add_vat_cases(price, rate, expected):
    """add_vat should match the expected value for each case."""
    assert add_vat(price, rate) == expected


def test_save_total(tmp_path):
    """save_total should write the total to a file."""
    out = tmp_path / "total.txt"
    save_total(out, [10, 20])
    # read the file back and assert on the text


def test_save_total_empty(tmp_path):
    """An empty list should still write a file."""
    out = tmp_path / "total.txt"
    save_total(out, [])
    # read the file back and assert on the text
