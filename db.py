from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = None
db = SQLAlchemy()