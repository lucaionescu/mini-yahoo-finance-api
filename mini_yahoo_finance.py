#!/usr/bin/env python

"""
Download and store historical stock data to a
Pandas dataframe using the Yahoo! Finance API.
"""

import re
from datetime import date
from time import mktime, sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup


HEADER = {
    'Connection': 'keep-alive',
    'Expires': '-1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
}


def _create_pandas_df(website_text):
    """Parse the scraped text to a
    Pandas Dataframe.

    Parameters
    ----------
    website_text : str

    Returns
    -------
    pd.core.frame.DataFrame
    """
    records = website_text.split('\n')[:-1]
    records = [(record.split(',')) for record in records]
    df = pd.DataFrame(records[1:], columns=records[0])
    return df


def _get_crumb_and_cookies(stock):
    """Collect the crumb and cookies needed
    for scraping

    Parameters
    ----------
    stock : str
        Stock name.

    Returns
    -------
    tuple
        Contains the crumb and cookies string.
    """
    url = f'https://finance.yahoo.com/quote/{stock}/history?p={stock}'
    r = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r.text, 'lxml')
    cookies = r.cookies
    crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))[0]
    return (crumb, cookies)


def _parse_date_to_unix(date_):
    """Parse a date string to an integer.

    Parameters
    ----------
    date_ : string
        Date string following the format DD-MM-YYYY

    Returns
    -------
    int
        Date represented as integer
    """
    return int(mktime(date_.timetuple()))


def get_stock_df(stock_name, start_date, end_date=None, interval='1d', max_retries=3):
    """Organizes the scraping process.

    Parameters
    ----------
    stock_name : string
        Stock name.
    start_date : datetime.date
        Start date.
    end_date : datetime.date, optional
        End date. If not given, the default is today.
    interval : string, optional
        Stock value interval, by default '1d'.
    max_retries : integer, optional
        Number of retries of failed requests, by default '3'.

    Returns
    -------
    pd.core.frame.DataFrame
        Pandas DataFrame containg the stock values.

    Raises
    ------
    ValueError
        Is raised when the start_date is after the end_date.
    ValueError
        Is raised when interval is not one of the supported values:
        [1d, 1wk, 1mo].
    """
    if end_date is None:
        end_date = date.today()

    if start_date > end_date:
        raise ValueError('start_date is has a more recent value than end_date.')

    if interval not in ['1d', '1wk', '1mo']:
        raise ValueError('unknown interval. Accepted values are [1d, 1wk, 1mo].')

    if not isinstance(max_retries, int) or max_retries <= 0:
        raise ValueError(
            'invalid value of max_retries. Accepted values are integers > 0.'
        )

    start_date = _parse_date_to_unix(start_date)
    end_date = _parse_date_to_unix(end_date)

    for i in range(max_retries):
        crumb, cookies = _get_crumb_and_cookies(stock_name)

        if len(crumb) != 11:
            sleep(i * 5)
            continue

        url = f'https://query1.finance.yahoo.com/v7/finance/download/{stock_name}?period1={start_date}&period2={end_date}&interval={interval}&events=history&crumb={crumb}'
        r = requests.get(url, headers=HEADER, cookies=cookies)
        df = _create_pandas_df(r.text)
        break

    return df
