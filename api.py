from flask import Flask
from flask_jwt_extended import JWTManager
import user.userview as userview
import talk.talkview as talkview
import test.testview
from flask_cors import *  # 导入模块
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

app.register_blueprint(userview.user)
app.register_blueprint(talkview.talker1)
app.register_blueprint(test.testview.bp_test)

CORS(app, supports_credentials=True)  # 设置跨域
if __name__ == "__main__":
    app.run(debug=True,port=5000)
