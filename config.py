import os
from sqlalchemy import create_engine
import urllib

class Config(object):
  SECRET_KEY = "21000028UTL"
  SESSION_COOKIE_SECURE = False
  
class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://IDGS801:1234@127.0.0.1:3306/pruebaFlask"
  SQLALCHEMY_TRACK_MODIFICATIONS = False