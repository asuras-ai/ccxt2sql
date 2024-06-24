import ccxt
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

class CCXTScraper:
    def __init__(self, exchanges, tickers, timeframes, db_url):
        self.exchanges = exchanges
        self.tickers = tickers
        self.timeframes = timeframes
        self.engine = create_engine(db_url)

    def fetch_ohlcv(self, exchange_name, ticker, timeframe):
        exchange = getattr(ccxt, exchange_name)()
        data = exchange.fetch_ohlcv(ticker, timeframe)
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df

    def store_ohlcv(self, exchange_name, ticker, timeframe, df):
        table_name = f"{exchange_name}_{ticker.replace('/', '_')}_{timeframe}"
        df.to_sql(table_name, self.engine, if_exists='append', index=False)
        with self.engine.connect() as conn:
            conn.execute(f"SELECT create_hypertable('{table_name}', 'timestamp', if_not_exists => TRUE)")

    def run_initial_import(self):
        for exchange in self.exchanges:
            for ticker in self.tickers:
                for timeframe in self.timeframes:
                    df = self.fetch_ohlcv(exchange, ticker, timeframe)
                    self.store_ohlcv(exchange, ticker, timeframe, df)

    def run_daily_update(self):
        for exchange in self.exchanges:
            for ticker in self.tickers:
                for timeframe in self.timeframes:
                    df = self.fetch_ohlcv(exchange, ticker, timeframe)
                    last_timestamp = df['timestamp'].max()
                    df = df[df['timestamp'] > last_timestamp]
                    self.store_ohlcv(exchange, ticker, timeframe, df)
