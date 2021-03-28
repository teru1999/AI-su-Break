from flask import Flask,render_template, request

from python_packages import core, freq, trend, recommend, create_model
from static import getimage

#Flaskオブジェクトの生成
app = Flask(__name__)

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