from distutils.command.config import config
from distutils.debug import DEBUG

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = "localhost"
    MySQL_USER = "tdea"
    MySQL_PASSWORD = ""
    MySQL_DB = ""

config = {"development": DevelopmentConfig}