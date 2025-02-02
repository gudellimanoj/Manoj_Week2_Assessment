# •	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass
    @abstractmethod
    def update(self, data_id, updated_data):
        pass
    @abstractmethod
    def delete(self, data_id):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        return f"Data inserted in SQL database: {data}"
    def update(self, data_id, updated_data):
        return f"Data updated in SQL database: {data_id} with {updated_data}"
    def delete(self, data_id):
        return f"Data deleted from SQL database: {data_id}"
class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        return f"Data inserted in NoSQL database: {data}"
    def update(self, data_id, updated_data):
        return f"Data updated in NoSQL database: {data_id} with {updated_data}"
    def delete(self, data_id):
        return f"Data deleted from NoSQL database: {data_id}"
sql=SQLDatabase()
print(sql.insert({"name":"manu","age":18}))
print(sql.update(1,{"name":"manu","age":20}))
print(sql.delete(1))
nosql=NoSQLDatabase()
print(nosql.insert({"name":"manu","age":18}))
print(nosql.update(1,{"name":"manu","age":19}))
print(nosql.delete(1))
