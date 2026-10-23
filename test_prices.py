"""Tests for prices.py."""

from pathlib import Path

import pytest

from prices import load_prices

SAMPLE = Path(__file__).parent / "sample_data" / "prices.csv"


def test_load_prices_sample():
    """Good rows load, bad rows are skipped."""
    prices = load_prices(SAMPLE)
    # assert on the whole dict
    assert prices == {"apple": 0.5, "bread": 1.2, "cheese": 3.5}


def test_load_prices_header_only(tmp_path):
    """A file with only a header gives an empty dict."""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("name,price\n", encoding="utf-8")
    # call load_prices on csv_file, then assert on the result
    assert load_prices(csv_file) == {}


def test_load_prices_not_found(tmp_path):
    csv_file = tmp_path / "nope.csv"
    with pytest.raises(FileNotFoundError):
        load_prices(csv_file)
