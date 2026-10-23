"""Tiny shop helpers used to practise testing."""


def add_vat(price, rate=0.2):
    """Return price with VAT added, rounded to 2 places."""
    if price < 0:
        raise ValueError("price cannot be negative")
    return round(price * (1 + rate), 2)


def save_total(path, prices):
    """Write the total of prices, with VAT added, to a text file."""
    total = sum(add_vat(p) for p in prices)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Total: {total:.2f}\n")


if __name__ == "__main__":
    print(add_vat(10))
    print(add_vat(0))
