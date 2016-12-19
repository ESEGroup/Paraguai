import os

class Config():
    SECRET_KEY = 'notthatsecret'
    EMAIL_ADAPTER = 'console'

class HerokuConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    EMAIL_ADATER = 'gmail'
    GMAIL_USER = os.environ.get('GMAIL_USER')
    GMAIL_PASS = os.environ.get('GMAIL_PASS')
