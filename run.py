from flask import jsonify
from flask_restful import Api
from server.app import app
from server.routes import router

api = Api(app)
router(api)


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to hellobooks'})


@app.route('/api/user')
def user():
    return 'this returns all the users'


if __name__ == '__main__':
    app.run()
