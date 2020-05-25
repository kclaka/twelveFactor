from flask import Flask, jsonify

# instatiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelpmentConfig')


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
