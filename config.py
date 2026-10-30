from datetime import timedelta
import os

'''
This file controls the variables for any configurations in Flask that I may want to use
later on in the development of the website
'''

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

    #Just like with secret key above - I'm going to replace placeholders with environment variables
    DB_NAME = "database"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = f"{os.environ['HOME']}/Downloads"

    SESSION_COOKIE_SECURE = True #Cookies are transferred if connected to HTTPS 

    SESSION_COOKIE_SAMESITE="None"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:////users.sqlite3"
    )


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PERMANENT_SESSION_TIME = timedelta(hours=3)

class ProductionConfig(Config):
    #Inherits all data and attributes of config class
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    #Sets debugging to true to enable reload of server

    DB_NAME = "todo"
    DB_USERNAME = "todouser"
    DB_PASSWORD = "flask"

    UPLOADS = f"{os.environ['HOME']}/Downloads"

class TestingConfig(Config):
    TESTING = True
    #Allows the user to test functionality

    DB_NAME = "testing"
    DB_USERNAME = "example"
    DB_PASSWORD = "test"

    UPLOADS = f"{os.environ['HOME']}/Downloads"

    SESSION_COOKIE_SECURE = False

    PERMANENT_SESSION_TIME = timedelta(minutes=55)