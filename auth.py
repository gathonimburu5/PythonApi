from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, Users
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

auth_nc = Namespace('auth')

#register user serializer
register_model = auth_nc.model(
    'Signup',
    {
        'Id': fields.Integer(),
        'FullNames': fields.String(),
        'Username': fields.String(),
        'Password': fields.String(),
        'EmailAddress': fields.String(),
        'PhoneNumber': fields.String(),
        'DateOfBirth': fields.Date(),
        'ProfilePicture': fields.String(),
        'Address': fields.String(),
        'CreatedOn': fields.Date()
    }
)
#login user serializer
login_model = auth_nc.model(
    'Login',
    {
        'Username': fields.String(),
        'Password': fields.String()
    }
)

@auth_nc.route("/signup")
class SignupResource(Resource):
    method_decorators = [jwt_required()]
    @auth_nc.marshal_with(register_model, code = 200)
    @auth_nc.expect(register_model)
    @jwt_required()
    @auth_nc.doc(security = "jsonWebToken")
    def post(self):
        data = request.get_json()
        register_data = Users(
            FullNames = data.get('FullNames'),
            Username = data.get('Username'),
            Password = generate_password_hash(data.get('Password')),
            EmailAddress = data.get('EmailAddress'),
            PhoneNumber = data.get('PhoneNumber'),
            DateOfBirth = data.get('DateOfBirth'),
            ProfilePicture = data.get('ProfilePicture'),
            Address = data.get('Address')
        )
        db.session.add(register_data)
        db.session.commit()
        return register_data, 200

@auth_nc.route("/login")
class LoginResource(Resource):
    @auth_nc.marshal_with(login_model, code = 200)
    @auth_nc.expect(login_model)
    def post(self): 
        data = request.get_json()
        Username = data.get('Username')
        Password = data.get('Password')
        
        data_user = Users.query.filter_by(Username = Username).first()
        if data_user and check_password_hash(data_user.Password, Password):
            access_token = create_access_token(identity=data_user.Username)
            refresh_token = create_refresh_token(identity=data_user.Username)
            return jsonify({ "access_token":access_token, "refresh_token": refresh_token })
