import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nathangwaro17@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://studiopx:12345@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    CSRF_ENABLED = True
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://studiopx:12345@localhost/pitch'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nathangwaro17@localhost/pitch'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}