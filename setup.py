from setuptools import setup

setup(name='mini_yahoo_finance_api',
      version='0.0.4',
      author='Luca Ionescu',
      url='https://github.com/lucaionescu/mini-yahoo-finance-api.git',
      author_email='ionescu@mailbox.org',
      description='Download and store historical stock data to a Pandas dataframe using the Yahoo! Finance API.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      license='MIT',
      keywords='yahoo finance stocks market',
      packages=['mini_yahoo_finance_api'],
      install_requires=[
          'BeautifulSoup',
          'pandas',
          'requests'
      ],
      zip_safe=False)
