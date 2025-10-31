from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    name = data['name']
    message = data['message']
    timestamp = datetime.now().strftime("%I:%M %p")  # 12-hour format
    emit('receive_message', {'name': name, 'message': message, 'time': timestamp}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
