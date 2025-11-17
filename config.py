import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "#TONOHUB"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "pizza_site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
