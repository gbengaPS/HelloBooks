from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import create_access_token
from server.models.users import User


class UserSignup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help='email field is required')
        parser.add_argument('full_name', required=True, help='full_name field is required')
        parser.add_argument('username', required=True, help='username field is required')
        parser.add_argument('password', required=True, help='password field is required')
        parser.parse_args()
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        user = User(full_name, username, email, password)
        check_user = user.check_username_email(username, email)
        if check_user == None:
            user.save()
            user_details = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': user.full_name
            }
            token = create_access_token(identity=user.id)
            return {'message': 'User created successfully','user': user_details, 'token': token}
        else:
            if check_user.username == username:
                return {'message': 'Username already in use'}, 409
            else:
                return {'message': 'Email already in use'}, 409
    def get(self):
        return 'this returns all users'

