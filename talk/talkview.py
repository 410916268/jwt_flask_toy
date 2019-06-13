from flask import Blueprint,request,jsonify
from talk import talker
from flask_jwt_extended import jwt_required,get_jwt_identity
import queue

talker1 = Blueprint('talker1',__name__)
QUEUE_DICT = {}
ROOM_DICT = {}  #key 群名称  value 群成员列表

@talker1.route('/createRoom',methods=['Post'])
@jwt_required
def createRoom():
    try:
        if not request.is_json:
            return jsonify({'msg':"params is not a json!"})
        className = request.json.get('className')
        classmates = request.json.get('classmates')  #['zhangsan','lisan']
        ROOM_DICT[className] = classmates
    except Exception as e:
        print(e)

@talker1.route('/talkToPeer',methods=['POST'])
@jwt_required
def talkToPeer():
    try:
        current_user = get_jwt_identity()
        if not request.is_json:
            return jsonify({'msg':"params is not a json!"})
        content = request.json.get('content')
        className = request.json.get('className')
        for user in ROOM_DICT[className]: # classmates = ROOM_DICT[className]
            QUEUE_DICT[user] = queue.Queue()
            q = QUEUE_DICT[user]
            q.put([current_user, content])
        return jsonify({"msg": "Talk to Peer successfully!"})
    except Exception as E:
        print(E)

@talker1.route('/getMsg',methods=['Get'])
@jwt_required
def getMsg():
    current_user = get_jwt_identity()
    q = QUEUE_DICT[current_user]
    ret = {}
    try:
        conntentFromPeer = q.get(timeout=5)     # 异常就夯(hang)住5秒
        ret["data"] = conntentFromPeer
        ret["msg"] = "接收成功"
    except Exception as E:
        print(E)
        ret["msg"] = "没接收到数据"
    return jsonify(ret)




