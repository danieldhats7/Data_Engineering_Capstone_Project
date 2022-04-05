from cfg import OLTP_URL
from constants import OLTP_NAME, BASE_FILE_DIR
import requests


class Extract:
    file_path_crib = (
        "{type}/{name}.csv"
    )
    def __init__(self, type_, name, url):
        self.type = type_
        self.url = url
        self.name = name

    def extract(self):
        """Extract data from url, stores it on file_path and return a transformed csv path location

        Returns:
            str: transformed csv path location
        """
        file_path = self.file_path_crib.format(type=self.type, name=self.name)
        m_path = BASE_FILE_DIR / file_path
        m_path.parent.mkdir(parents=True, exist_ok=True)

        r = requests.get(self.url)
        r.encoding = "utf-8"

        with open(m_path, "w") as f_out:
            f_out.write(r.text)

        return m_path

    def transform(self, df):

        return df
