from flask_restful import Api
from server.app import app
from server.routes import router



api = Api(app)
router(api)
if __name__ == '__main__':
    app.run()
