#!/usr/bin/env python

"""
Download and store historical stock data to a
Pandas dataframe using the Yahoo! Finance API.
"""

import io
import re
from datetime import datetime
from time import mktime

import pandas as pd
import requests
from bs4 import BeautifulSoup


_HEADER = {'Connection': 'keep-alive',
           'Expires': '-1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
           }


def _create_pandas_df(website_text):
    records = website_text.split('\n')[:-1]
    records = [(record.split(',')) for record in records]
    df = pd.DataFrame(records[1:], columns=records[0])
    return df


def _get_crumb_and_cookies(stock_name):
    url = f'https://finance.yahoo.com/quote/{stock_name}/history?p={stock_name}'
    r = requests.get(url, headers=_HEADER)
    soup = BeautifulSoup(r.text, 'lxml')
    cookies = r.cookies
    crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))[0]
    return (crumb, cookies)


def _parse_date_to_unix(date):
    return int(mktime(date.timetuple()))


def get_stock_dataframe(stock_name, start_date, end_date, interval='1d'):
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')

    if start_date > end_date:
        raise ValueError('start_date is has a more recent value than end_date.')

    if interval not in ['1d', '1wk', '1mo']:
        raise ValueError('unknown interval. Accepted values are [1d, 1wk, 1mo]')

    start_date = _parse_date_to_unix(start_date)
    end_date = _parse_date_to_unix(end_date)

    crumb, cookies = _get_crumb_and_cookies(stock_name)

    url = f'https://query1.finance.yahoo.com/v7/finance/download/{stock_name}?period1={start_date}&period2={end_date}&interval={interval}&events=history&crumb={crumb}'
    r = requests.get(url, headers=_HEADER, cookies=cookies)
    df = _create_pandas_df(r.text)
    return df
