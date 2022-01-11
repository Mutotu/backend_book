from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String)
  bikes=db.relationship("Bike_Post")
  bikes_saved = db.relationship("Bikes_Saved")
  
#   delete password when encriptions is read
  def to_json(self):
    return {
      "id": self.id,
      "username":self.username,
      "email": self.email,
      # "password":self.password
    }
    
    
class Bike_Post(db.Model):
    __tablename__ = 'bike_post'
    id=db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String, nullable=False)
    make=db.Column(db.String, nullable=False)
    model=db.Column(db.String, nullable=False)
    year=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    availability=db.Column(db.String, nullable=False)
    comments=db.Column(db.String, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('Bikes_Saved', secondary="user")
    def to_json(self):
        return{
            "id": self.id,
            "photo":self.photo,
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
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    bike_post_id=db.Column(db.Integer, db.ForeignKey('bike_post.id'))
    
    def to_json(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "bike_post_id":self.bike_post_id
        }
    