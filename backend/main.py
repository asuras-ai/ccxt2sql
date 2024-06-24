from flask import Flask, jsonify, request
from ccxt_handler import CCXTScraper
from sqlalchemy import create_engine, inspect
import schedule
import time

app = Flask(__name__)

exchanges = ['binance', 'kraken']
tickers = ['BTC/USDT', 'ETH/USDT']
timeframes = ['1d', '1h']
db_url = "postgresql://user:password@timescaledb/ohlcv"

scraper = CCXTScraper(exchanges, tickers, timeframes, db_url)

# Initial import
scraper.run_initial_import()

# Schedule daily updates
schedule.every().day.at("00:00").do(scraper.run_daily_update)

@app.route('/api/data_info', methods=['GET'])
def get_data_info():
    engine = create_engine(db_url)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    data_info = []

    with engine.connect() as conn:
        for table in tables:
            result = conn.execute(f"SELECT MIN(timestamp), MAX(timestamp) FROM {table}")
            first_timestamp, last_timestamp = result.fetchone()
            data_info.append({
                'table': table,
                'first_timestamp': first_timestamp,
                'last_timestamp': last_timestamp
            })

    return jsonify(data_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Keep the scheduling running in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

import threading
schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.start()
