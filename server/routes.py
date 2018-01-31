from server.controllers.users.authentication.signup import UserSignup
from server.controllers.users.authentication.login import UserLogin



def router(api):
    api.add_resource(UserSignup, '/api/user/signup')
    api.add_resource(UserLogin, '/api/user/login')