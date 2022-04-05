from cfg import OLTP_URL
from constants import OLTP_NAME
from extract import Extract
from load import Loader
import pandas as pd

load_ = Loader()


def extract(type, name, url):
    ext = Extract(type_=type, name=name, url=url)
    ext_path = ext.extract()
    return ext_path


def load(path):
    df = pd.read_csv(path, names=["product_id", "customer_id", "price", "quantity", "timestamp"])
    load_.load_table(df)


def run_pipeline():
    file_path = extract(type="OLTP", name=OLTP_NAME, url=OLTP_URL)
    load(file_path)


if __name__ == "__main__":
    run_pipeline()