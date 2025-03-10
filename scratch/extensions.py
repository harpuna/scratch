from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

"""
What the heck is this??

All extensions here are used as singletons and initialized in application factory
This makes references cleaner and avoids circular imports

Example from model:

    from app import db
    name = db.Column(db.Text)

Which is cleaner and more contolled than:

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
    name = db.Column(db.Text)
"""

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
migrate = Migrate()
