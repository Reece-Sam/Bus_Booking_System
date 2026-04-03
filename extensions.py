from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "pool_recycle": 280
}