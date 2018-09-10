from app import db
from .models import Property

class PropertyRepository:

    @staticmethod
    def create(property):
        db.session.add(property)
        db.session.commit()

    def find_by_id(id):
        return Property.query.get(id);


    