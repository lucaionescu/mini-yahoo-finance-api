# Minimal Yahoo! Finance API

A minimal library for downloading stock data from Yahoo! Finance into a Pandas DataFrame.

Since I am using this functionality for some time now, I thought I might as well write up this code nicely into a library and make it available.

## Example
```python
from mini_yahoo_finance import get_stock_df

df = get_stock_df(stock_name='ADS.DE',
		  start_date='01-01-2018',
	          end_date='31-01-2018',
		  interval='1d')
```

## Usage
Accepted values for `interval` are:
- `1d` (default)
- `1wk`
- `1mo`

If no `end_date` is provided, the current date will be used.

## Installation
```
pip install mini-yahoo-finance
```

## Requirements
- BeautifulSoup
- Pandas
- Requests

## Possible future to-dos
- remove BeautifulSoup dependency
- bulk download of multiple stocks using multithreading

Suggestions or problems? Don't hesitate to contact me or open a pull request!
