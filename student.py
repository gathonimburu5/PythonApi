from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Student

student_ns = Namespace('student')

# student serializer
student_model = student_ns.model(
    'Student',
    {
        'Id':fields.Integer(),
        'FullNames':fields.String(),
        'EmailAddress': fields.String(),
        'Phone':fields.String(),
        'Address':fields.String(),
        'County': fields.String(),
        'CreatedOn': fields.Date()
    }
)

@student_ns.route("/students")
class Students(Resource):
    @student_ns.marshal_list_with(student_model, code = 200, envelope = "students")
    def get(self):
        students = Student.query.all()
        # studen = text(""" select * from student  """)
        return students, 200 
    
    @student_ns.marshal_with(student_model, code = 200, envelope = "student")
    def post(self):
        data = request.get_json()
        fullName = data.get('FullNames')
        emailAddress = data.get('EmailAddress')
        phone = data.get('Phone')
        address = data.get('Address')
        county = data.get('County')

        new_student = Student(FullNames = fullName, EmailAddress = emailAddress, Phone = phone, Address = address, County = county)
        db.session.add(new_student)
        db.session.commit()
        return new_student, 200

@student_ns.route("/students/<int:id>")
class StudentsResource(Resource):
    @student_ns.marshal_with(student_model, code = 200, envelope = "student")
    def get(self, id):
        student = Student.query.get_or_404(id)
        return student, 200
    
    @student_ns.marshal_with(student_model, code = 200, envelope = "student")
    def put(self, id):
        student_to_update = Student.query.get_or_404(id)
        data = request.get_json()
        student_to_update.FullNames = data.get('FullNames')
        student_to_update.EmailAddress = data.get('EmailAddress')
        student_to_update.Phone = data.get('Phone')
        student_to_update.Address = data.get('Address')
        student_to_update.County = data.get('County')

        db.session.commit()
        return student_to_update, 200

    @student_ns.marshal_with(student_model, code = 200, envelope = "student")
    def delete(self, id):
        student_to_delete = Student.query.get_or_404(id)
        db.session.delete(student_to_delete)
        db.session.commit()
        return student_to_delete, 200
