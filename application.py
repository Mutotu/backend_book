import os
from flask import Flask, request
from flask_cors import CORS
import sqlalchemy
app = Flask(__name__)
CORS(app)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import jwt
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
import models
models.db.init_app(app)

def root():
  return 'ok'
app.route('/', methods=["GET"])(root)

# def create_user():
  
# Create a new post
@app.route('/createPost/<int:id>', methods=["POST"])
def create_post(id):
  try:
      post = models.Bike_Post(
      photo=request.json["photo"],
      make = request.json["make"],
      model = request.json["model"],
      year = request.json["year"],
      price = request.json["price"],
      availability = request.json["availability"],
      comments = request.json["comments"]
      )
      post.user_id = id
      models.db.session.add(post)
      models.db.session.commit()
      
      print(post)
      return {
        "post": post.to_json()
      }
  except sqlalchemy.exc.IntegrityError:
    return {"message": "All fields should be filled"}, 400
      
# get all the posts
@app.route('/getAllPosts', methods=["GET"])
def all_posts():
  try:
    posts = models.Bike_Post.query.all()
    return {
      "posts": [p.to_json() for p in posts]
    }
  except sqlalchemy.exc.IntegrityError:
    return {"message": "Something went wrong"}, 402
    

# delete a post a user created
@app.route('/deletePost/<int:bike_id>', methods=["DELETE"])
def delete_post(bike_id):
  try:
    post = models.Bike_Post.query.filter_by(id=bike_id).first()
    models.db.session.delete(post)
    models.db.session.commit()
    return {"deleted post": post.to_json()}
  except sqlalchemy.exc.IntegrityError:
    return {"message": "Something went wrong"}, 402


# update a post
@app.route('/updatePost/<int:bike_id>', methods=["PUT"])
def update_post(bike_id):
  try:
    post = models.Bike_Post.query.filter_by(id=bike_id).first()
    post.photo = request.json["photo"]
    post.make = request.json["make"]
    post.model = request.json["model"]
    post.year = request.json["year"]
    post.price = request.json["price"]
    post.availability = request.json["availability"]
    post.comments = request.json["comments"]
    
    models.db.session.add(post)
    models.db.session.commit()
    return {'post updated': post.to_json()}
  except sqlalchemy.exc.IntegrityError:
    return {"message": "Something went wrong"}, 402


if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run('0.0.0.0', port=port, debug=True)