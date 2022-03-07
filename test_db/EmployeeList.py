import psycopg2
import pandas as pd
import logging


class EmployeeList:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging
        try:
            self.connection = psycopg2.connect(database="test_postgres", user="poulomichandra", password="postgres",
                                          host="localhost", port=5432)
            self.logger.info(msg="Database successfully connected.")
        except:
            self.logger.warning(msg="Could not connect to database.")

    def list_employees(self):
        try:
            cur = self.connection.cursor()
            cur.execute(
                "SELECT t1.empno as EmployeeNumber, t1.ename as EmployeeName, t2.ename as Manager FROM emp t1, emp t2 "
                "WHERE t1.mgr=t2.empno;")
            rows = cur.fetchall()
            c1 = []
            c2 = []
            c3 = []

            for row in rows:
                temp_list = list(row)
                c1.append(temp_list[0])
                c2.append(temp_list[1])
                c3.append(temp_list[2])
            df = pd.DataFrame({'Employee No': c1, 'Employee Name': c2, 'Manager': c3})
            writer = pd.ExcelWriter('/Users/poulomichandra/Documents/Assignments/PythonSQLAssignment/test_db/PostgresSQL_q1.xlsx')
            df.to_excel(writer, sheet_name='Q1', index=False)
            writer.save()
            return 1

        except:
            self.logger.warning(msg="Execution unsuccessful. Exception occurred.")
            return 0

        finally:
            self.logger.info(msg="Execution Successful.")
            self.connection.close()
