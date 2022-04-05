from sqlalchemy import create_engine
from sqlalchemy import text
from constants import OLTP_NAME, SQL_DIR
from cfg import DB_CONNSTR

engine = create_engine(DB_CONNSTR)

def create_table():
    """ create db table """
    with engine.connect() as con:
        with open(SQL_DIR / f"{OLTP_NAME}.sql") as f:
            query = text(f.read())
        con.execute(f"DROP TABLE IF EXISTS {OLTP_NAME}")
        con.execute(query)

if __name__ == "__main__":
    create_table()