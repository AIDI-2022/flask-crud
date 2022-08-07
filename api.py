from students import *
from datetime import datetime

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'Students': Student.get_all_students()})

@app.route('/students/<int:id>', methods=['GET'])
def get_students_by_id(id):
    return_value = Student.get_student(id)
    return jsonify(return_value)

@app.route('/students', methods=['POST'])
def add_student():
    request_data = request.get_json() 
    Student.add_student(request_data["first_name"], request_data["last_name"],
                    request_data["dob"], request_data["amount_due"])
    response = Response("Student added", 201, mimetype='application/json')
    return response

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    request_data = request.get_json()
    Student.update_student(id, request_data['first_name'], request_data['last_name'], request_data['dob'], request_data["amount_due"])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response

@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    Student.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=8080, debug=True)