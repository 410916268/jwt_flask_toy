from flask import Flask
from flask_jwt_extended import JWTManager
import user.userview as userview
import talk.talkview as talkview
import test.testview
from flask_cors import *  # 导入模块

apk = Flask(__name__)
apk.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(apk)

apk.register_blueprint(userview.user)
apk.register_blueprint(talkview.talker1)
apk.register_blueprint(test.testview.bp_test)

CORS(apk, supports_credentials=True)  # 设置跨域
if __name__ == "__main__":
    apk.run(debug=True,port=5000)
