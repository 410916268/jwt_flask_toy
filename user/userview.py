from flask import Blueprint, jsonify,request
from flask_jwt_extended import  create_access_token
user = Blueprint('user',__name__)
users = {}
class User(object):
    def __init__(self,username, password):
        self.username = username
        self.password = password

@user.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username in users:
        return jsonify({"msg": "This username have been used!"}),201
    users[username]=User(username,password)
    return jsonify({"msg": "Signup success!"}), 200

@user.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg": "Missing username or password parameter"}), 400
    loginuser = users.get(username,None)
    if not loginuser:
        return jsonify({"msg": "User not exists"}), 401
    elif loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    else:
        return jsonify({"msg":"Password is incorrect!"}), 401