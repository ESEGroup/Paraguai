from flask import Blueprint, send_from_directory

assets = Blueprint('assets', __name__)

@assets.route('/<path:path>')
def send(path):
    return send_from_directory('assets', path)
