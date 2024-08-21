from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin='*')

@socketio.on('connect') #wrapper that triggers the following function on connect event
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect') #On disconnect event, the following function fires
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message') #when a message event is sent, the following function fires
def handle_message(message):
    print(f'Message Recieved: {message}')
    socketio.emit('message', message) #emit() is function that emits an event ('message) to all clients connected to the server

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)