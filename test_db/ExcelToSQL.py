import pandas as pd
from sqlalchemy import create_engine
import logging


class ExcelToSQL:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging
        try:
            self.engine = create_engine("postgresql+psycopg2://poulomichandra:postgres@localhost:5432/test_postgres")
            self.logger.info("Engine created successfully")
        except:
            self.logger.warning("Couldn't create engine")

    def read_sheets(self, data, file):
        try:
            if data == 'Q2':
                df = pd.read_excel(file, 'Q2')
                df.to_sql(name='compensation2', con=self.engine, if_exists='append', index=False)
            return 1

        except:
            self.logger.warning("Execution unsuccessful. Exception occurred.")
            return 0

        finally:
            self.logger.info("Execution Successful.")

    def convert_to_sql(self):
        result = 0
        with pd.ExcelFile('PostgresSQL_q2.xlsx') as xls:
            for sheet_name in xls.sheet_names:
                result = self.read_sheets(sheet_name, xls)
        return result

