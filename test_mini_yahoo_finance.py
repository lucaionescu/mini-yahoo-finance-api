import unittest
from datetime import date

from mini_yahoo_finance import get_stock_df


class TestMiniYahooFinance(unittest.TestCase):
    def test_get_stock_df(self):
        start_date = date(2021, 1, 1)
        end_date = date(2021, 1, 31)
        stock_name = 'ADS.DE'
        df = get_stock_df(stock_name, start_date, end_date)

        assert not df.empty

    def test_get_stock_df_2(self):
        start_date = date(2021, 1, 1)
        stock_name = 'ADE.DE'
        df = get_stock_df(stock_name, start_date)

        assert not df.empty

    def test_get_stock_df_3(self):
        start_date = date(2021, 1, 1)
        end_date = date(2021, 1, 31)
        stock_name = 'DTE.DE'
        df = get_stock_df(stock_name, start_date, end_date)

        assert not df.empty

    def test_get_stock_df_4(self):
        start_date = date(2021, 1, 31)
        end_date = date(2021, 1, 1)
        stock_name = 'ADS.DE'

        with self.assertRaises(ValueError):
            df = get_stock_df(stock_name, start_date, end_date)

    def test_get_stock_df_5(self):
        start_date = date(2021, 1, 1)
        end_date = date(2021, 1, 31)
        stock_name = 'ADS.DE'
        interval = '2d'

        with self.assertRaises(ValueError):
            df = get_stock_df(stock_name, start_date, end_date, interval=interval)

    def test_get_stock_df_6(self):
        start_date = date(2021, 1, 1)
        end_date = date(2021, 1, 31)
        stock_name = 'ADS.DE'
        df_1 = get_stock_df(stock_name, start_date, end_date, interval='1d')
        df_2 = get_stock_df(stock_name, start_date, end_date, interval='1wk')

        assert not df_1.empty
        assert not df_2.empty
        assert len(df_1) > len(df_2)


if __name__ == '__main__':
    unittest.main()
