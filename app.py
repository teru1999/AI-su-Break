import os
import json
import datetime
import random
import time

from flask import Flask,render_template, request
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from python_packages import core, freq, trend, recommend, create_model
from static import getimage


app = Flask(__name__)

@app.route('/publish')
def publish():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        
        while True:
            t = int(time.mktime(datetime.datetime.now().timetuple()))
            ws.send(json.dumps([{"time": t, "y": random.random() * 1000},
                                {"time": t, "y": random.random() * 1000}]))
            time.sleep(1)
    return

@app.route("/emotion", methods=['GET'])
def emotion():
    return render_template("emotion.html")

@app.route("/", methods=['GET'])
def index():
    filepath = 'rsc/tmp/talk.txt'

    trends = trend.main()
    freq_w = freq.main(filepath)
    create_model.main(freq_w)
    getimage.main(freq_w)
    recommend_w = recommend.main(freq_w)
    
    return render_template("index.html", freq = freq_w, trends = trends, recommend1 = recommend_w[0][0], recommend2 = recommend_w[1][0])

@app.route("/startstream", methods=['POST'])
def startstream():
    core.main()
    return render_template("index.html")

@app.route("/stopstream", methods=['POST'])
def stopstream():
    core.stop()
    return render_template("index.html")

@app.route("/update", methods=['POST'])
def update():
    filepath = 'rsc/tmp/talk.txt'

    trends = trend.main()
    freq_w = freq.main(filepath)
    create_model.main(freq_w)
    getimage.main(freq_w)
    recommend_w = recommend.main(freq_w)

    return render_template("index.html", freq = freq_w, trends = trends, recommend1 = recommend_w[0][0], recommend2 = recommend_w[1][0])

if __name__ == "__main__":
    app.run(debug=True)
    # app.debug = True
    # server = pywsgi.WSGIServer(('localhost', 8000), app, handler_class=WebSocketHandler)
    # server.serve_forever()
