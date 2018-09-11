import json
from app import db
from .models import Property, Province

class PropertyRepository:

    @staticmethod
    def create(property):
        db.session.add(property)
        db.session.commit()
        property.provinces = ProvinceRepository.find_province_by_lat_long(property.x,property.y)

    @staticmethod
    def find_by_id(id):
        prop = Property.query.get(id);
        if (prop):
            prop.provinces = ProvinceRepository.find_province_by_lat_long(prop.x,prop.y)
        return prop;

    @staticmethod
    def find_properties(upper_x, bottom_x, bottom_y, upper_y):
        filter_by_x = Property.x.between(upper_x, bottom_x)
        filter_by_y = Property.y.between(bottom_y, upper_y)
        
        result = Property.query.filter(filter_by_x).filter(filter_by_y).all()
        return  [PropertyRepository.include_provinces(p) for p in result]
            
    def include_provinces(p):
        p.provinces = ProvinceRepository.find_province_by_lat_long(p.x,p.y)
        return  p.as_dict()
    
class ProvinceRepository:

    def find_province_by_lat_long(x,y):
        return Province.find_by_x_y(x,y)


    