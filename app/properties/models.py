from app import db

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
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
