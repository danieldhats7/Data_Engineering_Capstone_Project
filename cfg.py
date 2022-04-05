from decouple import AutoConfig
from constants import ROOT_DIR

config = AutoConfig(search_path=ROOT_DIR)

DB_CONNSTR = config("DB_CONNSTR")

OLTP_URL = config("OLTP_DB")
