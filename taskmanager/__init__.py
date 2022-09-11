# this file makes sure to initialise the taskmanager application
# as a package

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# instance of of imported Flask() class
app = Flask(__name__)
# 2 app configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# instance of imported SQLAlchemy() class,
# set to instance of above Flask 'app'
db = SQLAlchemy(app)

# import file 'routes' from taskmanager package
from taskmanager import routes  # noqa