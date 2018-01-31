import os
from flask_restful import Api
from server.app import create_app
from flask_bcrypt import Bcrypt
from server.routes import router

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
api = Api(app)
bcrypt = Bcrypt(app)
router(api)
if __name__ == '__main__':
    app.run()
