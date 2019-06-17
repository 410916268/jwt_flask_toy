from flask import Flask
from flask_jwt_extended import JWTManager
import user.userview as userview
import talk.talkview as talkview
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

app.register_blueprint(userview.user)
app.register_blueprint(talkview.talker1)

# @app.route("/test",methods=["GET"])
# def test():
#     return "hello world"

if __name__ == "__main__":
    app.run(debug=True,port=5000)
