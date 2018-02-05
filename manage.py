import os
from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from server.app import DB, create_app
from server.models import users

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, DB)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
