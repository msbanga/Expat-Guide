from project import app
from flask import request, render_template


@app.route('/')  # at the end point /
def start():
    return render_template("home.html")


@app.route('/countries')  # at the end point /
def get_countries():
    from project.helpers.helper import Helper
    helper = Helper()
    response = helper.get_countries()
    return response


@app.route('/relevant_countries', methods=['GET', 'POST'])
def options():
    args = request.form
    from project.helpers.helper import Helper
    helper = Helper()
    response = helper.perform_operation(args)
    return response
