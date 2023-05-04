import mysql.connector

class MySQLDatabase:
    def __init__(self):
        self.database_name = 'emoloyeedb'
        self.connection = None
        self.connect()

        self.table_name = None
        self.column_names = None
        self.columns = None
        self.primary_key = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database=self.database_name
        )
        print("Connected to MySQL Database")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL Database")

    def execute_query(self, query):
        print(query)

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def create_table(self):
        column_str = ", ".join([f"{col[0]} {col[1]}" for col in self.columns])
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({column_str})"
        self.execute_query(query)

    def insert_data(self, values):
        query = f"INSERT INTO {self.table_name} {self.column_names} VALUES ({values})"
        self.execute_query(query)

    def delete_data(self, key):
        query = f"DELETE FROM {self.table_name} WHERE {self.primary_key} = {key}"
        self.execute_query(query)

    def update_on_primary_key(self, key, set_clause):
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {self.primary_key} = {key}"
        self.execute_query(query)

    def query_on_primary_key(self, key):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE {self.primary_key} LIKE '%{key}%'"
        cursor.execute(query, {"key": key})
        return cursor.fetchall()

    def get_distinct_primary_key(self):
        cursor = self.connection.cursor()
        query = f"SELECT DISTINCT({self.primary_key}) FROM {self.table_name}"
        cursor.execute(query)
        return cursor.fetchall()
class Employee(MySQLDatabase):
    def __init__(self):
        super().__init__()

        self.table_name = "employee"
        self.columns = [
            ("id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(255)"),
            ("address", "VARCHAR(255)"),
            ("phone", "VARCHAR(20)"),
            ("dob", "DATE"),
            ("department_id", "INT REFERENCES departments(id)"),
            ("salary_id", "INT REFERENCES salary(id)")
        ]
        self.column_names = "(name, address, phone, dob, department_id, salary_id)"
        self.primary_key = "id"
        self.create_table()

    def update_data(self, id, name, address, phone, dob, department_id, salary_id):
        set_clause = f"name = '{name}', address = '{address}', phone = '{phone}', dob = '{dob}', " \
                     f"department_id = {department_id}, salary_id = {salary_id}"
        condition = f"id = {id}"
        self.update_on_primary_key(set_clause, condition)

    def delete_employee(self, id):
        condition = f"id = {id}"
        self.delete_data(condition)
        
class Department(MySQLDatabase):
    def __init__(self):
        super().__init__()

        self.table_name = "departments"
        self.columns = [
            ("id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(255)"),
            ("description", "VARCHAR(255)")
            
        ]
        self.column_names = "(name, description)"
        self.primary_key = "id"
        self.create_table()

    def update_data(self, id, name, description, salary):
        set_clause = f"name = '{name}', description = '{description}'"
        condition = f"id = {id}"
        self.update_on_primary_key(set_clause, condition)

    def delete_department(self, id):
        condition = f"id = {id}"
        self.delete_data(condition)
        
class Salary(MySQLDatabase):
    def __init__(self):
        super().__init__()

        self.table_name = "salary"
        self.columns = [
            ("id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("employee_id", "INT REFERENCES employee(id)"),
            ("salary_amount", "DECIMAL(10,2)"),
            ("salary_date", "DATE")
        ]
        self.column_names = "(employee_id, salary_amount, salary_date)"
        self.primary_key = "id"
        self.create_table()

    def update_data(self, id, employee_id, salary_amount, salary_date):
        set_clause = f"employee_id = {employee_id}, salary_amount = {salary_amount}, " \
                     f"salary_date = '{salary_date}'"
        condition = f"id = {id}"
        self.update_on_primary_key(set_clause, condition)
    def delete_salary(self, id):
        condition = f"id = {id}"
        self.delete_data(condition)


a=MySQLDatabase()