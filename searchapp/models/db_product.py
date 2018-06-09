import json
import os

from sqlalchemy import Column, String, Numeric
from searchapp.models.base import Base


class Product():

    __tablename__ = 'products'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     description = Column(String)
     image = Column(String)
     taxonomy = Column(String)
     price = Column(Numeric)
