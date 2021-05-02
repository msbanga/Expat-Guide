from project import app
from flask import request


@app.route('/')  # at the end point /
def start():
    return 'Welcome Expat!'


@app.route('/countries')  # at the end point /
def get_countries():
    from project.helpers.helper import Helper
    helper = Helper()
    response = helper.get_countries()
    return response

@app.route('/relevant_countries')
def options():
    args = request.args
    from project.helpers.helper import Helper
    helper = Helper()
    response = helper.perform_operation(args)
    return response
