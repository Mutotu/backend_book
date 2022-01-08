from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String)
#   delete password when encriptions is read
  def to_json(self):
    return {
      "id": self.id,
      "email": self.email,
      "password":self.password
    }
    
    
class Bike_Post(db.Model):
    __tablename__ = 'bike_post'
    id=db.Column(db.Integer, primary_key=True)
    make=db.Column(db.String, nullable=False)
    model=db.Column(db.String, nullable=False)
    year=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    availability=db.Column(db.String, nullable=False)
    comments=db.Column(db.String, nullable=False)
    
    def to_json(self):
        return{
            "id": self.id,
            "make":self.make,
            "model":self.model,
            "year":self.year,
            "price":self.price,
            "availability":self.availability,
            "comments":self.comments
        }
        
        
class Bikes_Saved(db.Model):
    __tablename__= "bikes_saved"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer)
    bike_post_id=db.Column(db.Integer)
    
    def to_json(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "bike_post_id":self.bike_post_id
        }
    