from flask import Flask,render_template,request,redirect
from googletrans import Translator
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/trans",methods=["GET", "POST"])
def trans():
    if request.method == "POST":
     t_sentence = request.form["sentence"]
     language = request.form['inputvalue']
     output = Translator().translate(t_sentence, dest=language)
     text = output.text
    else:
        return render_template("home.html")
    return render_template('home.html',output=text,sentence=t_sentence)


if __name__ == '__main__':
    app.run(debug=True)
