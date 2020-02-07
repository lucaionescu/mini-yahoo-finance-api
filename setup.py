#!/usr/bin/env

from setuptools import setup

import mini_yahoo_finance


def get_readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='mini_yahoo_finance',
    version='0.0.7',
    author='Luca Ionescu',
    url='https://github.com/lucaionescu/mini-yahoo-finance-api.git',
    author_email='ionescu@mailbox.org',
    description='Download and store historical stock data to a Pandas dataframe using the Yahoo! Finance API.',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='yahoo finance stocks market',
    py_modules=['mini_yahoo_finance'],
    install_requires=['beautifulsoup4', 'pandas', 'requests'],
    zip_safe=False,
)
