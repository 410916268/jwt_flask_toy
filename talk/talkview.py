from flask import Blueprint,request,jsonify
from talk import talker
from flask_jwt_extended import jwt_required

talker1 = Blueprint('talker1',__name__)

@talker1.route('/talk',methods=['POST'])
@jwt_required
def talk():
    if not request.is_json:
        return jsonify({'msg':"params is not a json!"})
    SenFrom = request.json.get('sentence')
    return jsonify({'reply': talker.talk(SenFrom)})

