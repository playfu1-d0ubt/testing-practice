"""Read a price list from a CSV file."""

import csv


def load_prices(path):
    """Return {name: price} from a CSV with name and price columns.

    Rows with a missing name or a price that is not a number are skipped.
    Raises FileNotFoundError if the file does not exist.
    """
    prices = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = (row.get("name") or "").strip()
            try:
                price = float(row.get("price") or "")
            except ValueError:
                continue
            if name:
                prices[name] = price
    return prices
