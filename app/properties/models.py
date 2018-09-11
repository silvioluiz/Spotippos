from app import db
from .utils import load
import json

class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    baths = db.Column(db.Integer, nullable=False)
    squareMeters = db.Column(db.Integer, nullable=False)
    provinces = []
    
    def as_dict(self):
        colum_list = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        colum_list['provinces'] = self.provinces 
        return colum_list

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Province():
    
    def find_by_x_y(x, y):
        provinces = load('schemas/provinces.json')
        founded_provinces = [ k for k,v in provinces.items() 
            if(x >= v['boundaries']['upperLeft']['x'] and 
               x <= v['boundaries']['bottomRight']['x'] and
               y <= v['boundaries']['upperLeft']['y'] and 
               y >= v['boundaries']['bottomRight']['y']
            ) 
        ]
        return founded_provinces