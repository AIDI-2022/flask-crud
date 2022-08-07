from settings import *
import json
from datetime import datetime

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80))
    amount_due = db.Column(db.Integer, default = 0, nullable=False)

    def json(self):
        return {'student_id': self.student_id, 'first_name': self.first_name,
                'last_name': self.last_name, 'dob': self.dob, 'amount_due': self.amount_due}
    
    def add_student(_first_name, _last_name, _dob, _amount_due):

        new_student = Student(first_name=_first_name, last_name=_last_name, dob=_dob, amount_due = _amount_due )
        db.session.add(new_student)
        db.session.commit()

    def get_all_students():
        return [Student.json(student) for student in Student.query.all()]

    def get_student(_student_id):
        return [Student.json(Student.query.filter_by(student_id=_student_id).first())]

    def update_student(_student_id, _first_name, _last_name, _dob, _amount_due):
        students_to_update = Student.query.filter_by(student_id=_student_id).first()
        students_to_update.first_name = _first_name
        students_to_update.last_name = _last_name
        students_to_update.dob = _dob
        students_to_update.amount_due = _amount_due
        db.session.commit()

    def delete_student(_student_id):
        Student.query.filter_by(student_id=_student_id).delete()
        db.session.commit()