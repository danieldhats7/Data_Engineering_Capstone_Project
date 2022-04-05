from sqlalchemy import create_engine
import pandas as pd
from constants import OLTP_NAME
from cfg import DB_CONNSTR

engine = create_engine(DB_CONNSTR)

class Loader:
    def load_table(self, df):
        df.to_sql(OLTP_NAME, con=engine, index=False, if_exists="append")
    