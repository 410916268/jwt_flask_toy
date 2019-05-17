from flask import Blueprint

bp_test = Blueprint('bp_test',__name__)

@bp_test.route('/test',methods=['POST'])
def test():
    return 'hello'