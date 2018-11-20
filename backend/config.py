import os
class BaseConfig(object):
    DEBUG = True
    ## ここを追記
    SQLALCHEMY_DATABASE_URI = 'sqlite:///backend.db'
    # cookieを暗号化する秘密鍵
    SECRET_KEY = os.urandom(24)
