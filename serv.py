from flask import Flask, render_template, request, session
from datetime import datetime
import flask_socketio as si
# Import modules.
import wave
import base64
import numpy
# audio => freqCode => area => evacuation route
# TODO: Create the area-frequency code list (json)
# TODO: Implement the area-freqCode match module
# TODO: Implement the area-evacRoute module

app = Flask(__name__)
app.secret_key = "Random string"
socketio = si.SocketIO(app, manage_session=False)

## Test
td = bytes()

@app.route('/')
def home():
    return render_template('audioTest.html')

# SOCKETIO FUNCTIONS

@socketio.on('idxTest')
def idxTest(idx):
    print(idx)

@socketio.on('periodic')
def periodicLoad(blob):
    global td
    #w = wave.Wave_read(blob)
    
    #print(w.getframerate())
    print(blob)
    td += blob['data']
    if blob['idx'] == 9:
        f = open('./file' + str(blob['idx']) + '.wav', 'wb')
        f.write(td)
        f.close()
#########

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')