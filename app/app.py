from flask import Flask, request, jsonify
import multiprocessing
from pipe import Pipe
from filters.filter_service import filter_service
from filters.screaming_service import screaming_service
from filters.publish_service import publish_service

app = Flask(__name__)

def start_filters():
    pipe1 = Pipe()
    pipe2 = Pipe()
    pipe3 = Pipe()
    pipe4 = Pipe()

    multiprocessing.Process(target=filter_service, args=(pipe1, pipe2)).start()
    multiprocessing.Process(target=screaming_service, args=(pipe2, pipe3)).start()
    multiprocessing.Process(target=publish_service, args=(pipe3, pipe4)).start()

    return pipe1, pipe4

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    user = data.get('user')
    if message and user:
        pipe1, pipe4 = start_filters()
        pipe1.push(f"{user}:{message}")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid data"}), 400