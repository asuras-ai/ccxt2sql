from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.engine import reflection

def create_database(db_url):
    engine = create_engine(db_url)
    metadata = MetaData()

    # Example of creating a table if it doesn't exist
    table = Table(
        'ohlcv_template', metadata,
        Column('timestamp', DateTime, primary_key=True),
        Column('open', Float),
        Column('high', Float),
        Column('low', Float),
        Column('close', Float),
        Column('volume', Float),
        extend_existing=True
    )

    metadata.create_all(engine)

    with engine.connect() as conn:
        insp = reflection.Inspector.from_engine(engine)
        if 'ohlcv_template' not in insp.get_table_names():
            conn.execute("SELECT create_hypertable('ohlcv_template', 'timestamp')")

if __name__ == "__main__":
    db_url = "postgresql://user:password@db/ohlcv"
    create_database(db_url)

