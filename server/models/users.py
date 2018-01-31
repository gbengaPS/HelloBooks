from server.app import DB, bcrypt
from server.models.base_model import BaseModel


class User(DB.Model, BaseModel):
    """This class represents the users table in the database"""
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    full_name = DB.Column(DB.String(255), nullable=False)
    username = DB.Column(DB.String(255), nullable=False, unique=True)
    email = DB.Column(DB.String(255), nullable=False, unique=True)
    password = DB.Column(DB.String(255), nullable=False)
    admin = DB.Column(DB.Boolean, default=False)
    created_at = DB.Column(
        DB.DateTime, default=DB.func.current_timestamp(),
        onupdate=DB.func.current_timestamp())

    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    def check_username_email(self, username, email):
        user = User.query.filter((User.username==username) | (User.email==email)).first()
        return user


