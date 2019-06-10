from flask import Blueprint,request,jsonify
from talk import talker
from flask_jwt_extended import jwt_required,get_jwt_identity
import queue

talker1 = Blueprint('talker1',__name__)
QUEUE_DICT = {}

@talker1.route('/talkToPeer',methods=['POST'])
@jwt_required
def talkToPeer():
    try:
        current_user = get_jwt_identity()
        if not request.is_json:
            return jsonify({'msg':"params is not a json!"})
        content = request.json.get('content')
        peer = request.json.get('peer')
        # QUEUE_DICT[peer] = queue.Queue()
        # QUEUE_DICT[current_user] = queue.Queue()
        for user in [peer,current_user]:
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




