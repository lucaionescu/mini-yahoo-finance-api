# Minimal Yahoo! Finance API

A minimal library for downloading stock data from Yahoo! Finance into a Pandas DataFrame.

Since I am using this functionality for some time now, I thought I might as well write up this code nicely into a library and make it available.

## Example
```python
from mini_yahoo_finance_api import get_stock_dataframe

df = get_stock_dataframe(stock_name='ADS.DE',
			 start_date='01-01-2018',
			 end_date='31-01-2018',
			 interval='1m')
```

## Usage
Accepted values for `interval` are: 
- `1d` (default)
- `1wk`
- `1mo`

## Installation
```
pip install mini-yahoo-finance-api
```

## Requirements
- BeautifulSoup
- Pandas
- Requests

## Possible future to-dos
- remove BeautifulSoup dependency
- bulk download of multiple stocks using multithreading
- add support for more output formats

Suggestions or problems? Don't hesitate to contact me or open a pull request!
