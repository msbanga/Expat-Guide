from project import app


@app.route('/')  # at the end point /
def start():
    return 'Hello World!'


@app.route('/countries')  # at the end point /
def get_countries():
    return 'Sweden Germany'
