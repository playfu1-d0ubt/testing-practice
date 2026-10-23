# Testing Practice

Small practice project for learning `pytest`. Two tiny modules, each with tests.

## What it does

- `shop.py`: adds VAT to a price (`add_vat`) and writes a total to a text file (`save_total`).
- `prices.py`: reads a CSV price list into a dictionary (`load_prices`). Rows with a missing name or a price that is not a number are skipped.
- `test_shop.py` and `test_prices.py`: 10 tests covering normal cases, edge cases and errors.

## How to run

```bash
git clone https://github.com/playfu1-d0ubt/testing-practice.git
cd testing-practice
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

All 10 tests should pass.

## What the tests cover

- Normal values, zero, and a custom VAT rate (one `parametrize` test with several cases).
- A negative price raises `ValueError`.
- Writing a file, using a temporary folder from `tmp_path`, so no real files are touched.
- An empty list gives a total of `0.00`.
- A sample CSV with bad rows (`sample_data/prices.csv`), a header-only file, and a missing file.

## Limitations

- Practice code, not a real shop system.
- `add_vat` is for single prices and has no currency handling.
- `load_prices` skips bad rows without saying so. A real tool should report them.
- Tests do not run automatically yet. GitHub Actions is the next step.

## What I learned

- A test is a small check that runs the same way every time.
- Write the test first, watch it fail, then fix the code.
- Read pytest output from the bottom: the last line says what went wrong.
- Use `tmp_path` so tests never touch real files.
- A test with no `assert` always passes, so break a test on purpose to check it works.
- `.gitignore` does not hide files git already tracks.