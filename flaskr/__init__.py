from functools import wraps
import os

from flask import Flask, jsonify, make_response, request, session
from flask_cors import CORS
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


import jwt


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy()
db.init_app(app)


JWT_SECRET_KEY = "seeecret"

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    date_registered = db.Column(db.DateTime, default = datetime.utcnow())

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return 'HELLO'

if __name__ == '__main__':
    app.run()

'''returns token'''
def encode_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=0, seconds=360),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm= 'HS256')
    return token

@app.route('/register', methods = ['POST'])
def register():
    user_data = request.get_json()
    user = User.query.filter_by(username = user_data['username']).first()
    if not user:
        try:
            hashed_password = generate_password_hash(user_data['password'])
            user = User(username = user_data['username'], password = hashed_password)
            db.session.add(user)
            db.session.commit()
            response = {
                "status":"success",
                "message":"User successfully registered"
            }
            return make_response(jsonify(response)),201
        except Exception as e:
            print(e)
            response = {
                "status":"error",
                "message":"Error occured, user registration failed"
            }
            return make_response(jsonify(response)),401
    else:
        response = {
            "status":"error",
            "message":"User already exists"
        }
        return make_response(jsonify(response)),202
    
@app.route('/login',methods = ['POST'])
def login():
    user_data = request.get_json()
    try:

        user = User.query.filter_by(username = user_data['username']).first()

        if user and check_password_hash(user.password,user_data['password'])==True:
            auth_token = encode_token(user.id)
            response = {
                "status":"success",
                "message" :"Successfully logged in",
                "auth_token":auth_token,
            }
            return make_response(jsonify(response)),200
        else:
            response = {
                "status":"Error",
                "message":"User does not exist"
            }
            return make_response(jsonify(response)), 404

    except Exception as e:
        print(e)
        response = {
            "Status":"error",
                "Message":"User login failed"
        }
        return make_response(jsonify(response)), 404

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            print(token)
        if not token:
            return {
                "message": "Authentication Token is missing",
                "error": "Unauthorized"
            }, 401
        try:
            data=jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            current_user=User().get_by_username(data["username"])
            if current_user is None:
                return {
                "message": "Invalid Authentication token",
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "An error Occured",
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/protected', methods=['GET'])
@token_required 
def protected():  
   
   resp = {"message":"This is a protected view"}   
   return make_response(jsonify(resp)), 404

@app.route('/users', methods = ['GET'])
@token_required
def getUser():
    user_data = request.headers.get('')