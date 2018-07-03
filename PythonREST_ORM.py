# codebase from: https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# I want to integrate this ORM for SQLite: https://github.com/coleifer/peewee
# quickstart at: http://docs.peewee-orm.com/en/latest/peewee/quickstart.html

from flask import Flask, request
from flask_restful import Resource, Api
from playhouse.shortcuts import model_to_dict
from sqlalchemy import create_engine
from json import dumps
import json
from flask import jsonify
from peewee import *


#db_connect = create_engine("sqlite:///chinook.db")
app = Flask(__name__)
api = Api(app)
db = SqliteDatabase("chinook.db")


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db


class Employees(BaseModel):
    EmployeeId = PrimaryKeyField()
    FirstName = CharField(null=False)
    LastName = CharField(null=False)

    class Meta:
        database = db


class GetEmployees(Resource):
    def get(self):
        db.connect()
        result = []
        for emp in Employees.select():
            result.append(emp)
        db.close()
        query_result = []
        for r in result: query_result.append(json.dumps(model_to_dict(r)))
        return query_result

# class Employees(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees")
#         return {"employees": [i[0] for i in query.cursor.fetchall()]}
#
#
# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)
#
#
# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d " % int(employee_id))
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)
#
#
# class DeleteEmployee(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         conn.execute("delete from employees where EmployeeId =%d " % int(employee_id))
#         query = conn.execute("select * from employees")
#         return {"employees": [i[0] for i in query.cursor.fetchall()]}

#Multiple parameters and visualization!
# class AddNew(Resource):
#     def get(self, firstname, lastname):
#         conn = db_connect.connect()
#         conn.execute("INSERT INTO employees('FirstName','LastName') VALUES (" + firstname + "," + lastname + ")")
#         query = conn.execute("select FirstName from employees")
#         return {"employees": [i[0] for i in query.cursor.fetchall()]}


api.add_resource(GetEmployees, '/employees')  # Route_1
# api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
# api.add_resource(DeleteEmployee, "/employees_rem/<employee_id>") #cancella imp
# api.add_resource(AddNew, "/addNew/<firstname>&<lastname>") #cancella imp

if __name__ == '__main__':
    app.run(port='5002')