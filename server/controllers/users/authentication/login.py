from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import create_access_token
from server.app import bcrypt
from server.models.users import User


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username field is required')
        parser.add_argument('password', required=True, help='password field is required')
        parser.parse_args()
        password = request.form['password']
        username = request.form['username']
        user = User.query.filter((User.username == username) | (User.email == username)).first()
        if not user:
            return {'message': 'username or password incorrect'}, 401
        else:
            if bcrypt.check_password_hash(user.password, password):
                user_details = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name
                }
                token = create_access_token(identity=user.id)
                return {'message': 'User login successful', 'user': user_details, 'token': token}
            else:
                return {'message': 'username or password incorrect'}, 401
