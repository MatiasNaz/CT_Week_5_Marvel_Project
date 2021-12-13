from flask import Flask
from config import Config

from flask_migrate import Migrate
from flask_login import LoginManager


from .models import db, User

# import our blueprints for registration
from .blog.routes import blog
from .auth.routes import auth


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)

from app import routes, models, auth
from .models import User, db

login = LoginManager()
db.init_app(app)
login.init_app(app)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(blog)
app.register_blueprint(auth)

# initialize our databse to work with our app
db.init_app(app)
login.init_app(app)