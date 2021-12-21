from flask import Flask, render_template, request
from googletrans import Translator
trans = Translator()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/translate')
def translate(data, srclang, destlang):
    mytext = data
  
    
    t = trans.translate(mytext,
    src = srclang ,
    dest = destlang)
    print(f'{t.origin}->{t.text}')
    outputText = f'{t.text}'  
    return render_template('home.html', outputText)    


if __name__=='__main__':
    app.run(debug=True)
