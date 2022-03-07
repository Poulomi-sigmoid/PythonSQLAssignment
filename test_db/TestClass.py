import pytest
from test_db.EmployeeList import EmployeeList
from test_db.ExcelToSQL import ExcelToSQL
from test_db.SQLtoExcel import SQLtoExcel


class TestClass:

    @classmethod
    def setup_class(cls):
        print("\nSetting Up Class")

    @classmethod
    def teardown_class(cls):
        print("\nTearing Down Class")

    @pytest.fixture()
    def employee_list(self):
        emp = EmployeeList()
        return emp

    @pytest.fixture()
    def sql_to_excel(self):
        sql_to_excel = SQLtoExcel()
        return sql_to_excel

    @pytest.fixture()
    def excel_to_sql(self):
        excel_to_sql = ExcelToSQL()
        return excel_to_sql

    def test_list_employees(self, employee_list):
        assert employee_list.list_employees() == 1

    def test_convert_sql_table_to_excel(self, sql_to_excel):
        assert sql_to_excel.convert_to_excel() == 1

    def test_convert_excel_to_sql_table(self, excel_to_sql):
        assert excel_to_sql.convert_to_sql() == 1


