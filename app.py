from flask import Flask,render_template,request,redirect,flash
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

@app.route("/contact",methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    subject = request.form['subject']
    message = request.form['message']
    return render_template('home.html', name=name)

@app.route("/subscribe",methods=["POST"])
def subscribe():
    email = request.form['email']
    return render_template('home.html',email=email)

if __name__ == '__main__':
    app.run(debug=True)
