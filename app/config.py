import os
#import app

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''

class Development(Config):
    MODE = 'Development'
    DEBUG = True
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:///{}".format(os.path.join(project_dir, "properties.db"))
    SQLALCHEMY_DATABASE_URI = database_file

class Production(Config):
    MODE = 'Production'
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = ''