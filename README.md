# Minimal Yahoo! Finance API


[![PyPI](https://img.shields.io/pypi/v/mini-yahoo-finance?style=plastic)](https://pypi.org/project/mini-yahoo-finance/)


A minimal library for downloading stock data from Yahoo! Finance into a Pandas DataFrame.

## Example
```python
from datetime import date
from mini_yahoo_finance import get_stock_df

start_date = date(2021, 1, 1)
end_date = date(2021, 1, 31)

df = get_stock_df(
    stock_name='ADS.DE',
    start_date=start_date,
    end_date=end_date,
    interval='1d',
    max_retries=3
)
```

## Usage
Accepted values for `interval` are:
- `1d` (default)
- `1wk`
- `1mo`

If no `end_date` is provided, the current date will be used.

## Installation
```
git clone https://github.com/lucaionescu/mini-yahoo-finance-api.git
cd mini-yahoo-finance-api/
pip install .
```

## Requirements
- BeautifulSoup
- Pandas
- Requests

Suggestions or problems? Don't hesitate to contact me or open a pull request!
