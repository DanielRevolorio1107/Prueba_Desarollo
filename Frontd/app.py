from flask import Flask, request, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

# In-memory data stores
employees = []
departments = [
    {"code": 1, "name": "HR"},
    {"code": 2, "name": "Engineering"},
    {"code": 3, "name": "Sales"}
]

# Helper functions
def find_employee_by_id(emp_id):
    return next((emp for emp in employees if emp['id'] == emp_id), None)

# RESTful API Resources
@api.route('/api/employees')
class EmployeeList(Resource):
    def get(self):
        return jsonify(employees)

    def post(self):
        data = request.json
        new_id = max(emp['id'] for emp in employees) + 1 if employees else 1
        data['id'] = new_id
        employees.append(data)
        return jsonify(data), 201

@api.route('/api/employees/<int:emp_id>')
class Employee(Resource):
    def get(self, emp_id):
        employee = find_employee_by_id(emp_id)
        if employee is None:
            return {"message": "Employee not found"}, 404
        return jsonify(employee)

    def put(self, emp_id):
        data = request.json
        employee = find_employee_by_id(emp_id)
        if employee is None:
            return {"message": "Employee not found"}, 404
        employee.update(data)
        return jsonify(employee)

    def delete(self, emp_id):
        global employees
        employees = [emp for emp in employees if emp['id'] != emp_id]
        return '', 204

@api.route('/api/departments')
class DepartmentList(Resource):
    def get(self):
        return jsonify(departments)

if __name__ == '__main__':
    app.run(debug=True)
