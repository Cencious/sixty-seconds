import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY ='2%W%@+kp%@mZJ'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kakan:Abiathar2022@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("kancencious@gmail.com")
    MAIL_PASSWORD = os.environ.get("edithaseyo#*")
    SUBJECT_PREFIX = 'sixty seconds Pitch'
    SENDER_EMAIL = 'kancencious@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kakan:Abiathar2022@localhost/pitch_test'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}