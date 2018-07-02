# codebase from: https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

db_connect = create_engine("sqlite:///chinook.db")
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from employees")
        return {"employees": [i[0] for i in query.cursor.fetchall()]}


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class DeleteEmployee(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        conn.execute("delete from employees where EmployeeId =%d " % int(employee_id))
        query = conn.execute("select * from employees")
        return {"employees": [i[0] for i in query.cursor.fetchall()]}

#Multiple parameters and visualization!
class AddNew(Resource):
    def get(self, firstname, lastname):
        conn = db_connect.connect()
        conn.execute("INSERT INTO employees('FirstName','LastName') VALUES (" + firstname + "," + lastname + ")")
        query = conn.execute("select FirstName from employees")
        return {"employees": [i[0] for i in query.cursor.fetchall()]}


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
api.add_resource(DeleteEmployee, "/employees_rem/<employee_id>") #cancella imp
api.add_resource(AddNew, "/addNew/<firstname>&<lastname>") #cancella imp

if __name__ == '__main__':
    app.run(port='5002')