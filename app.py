from flask import Flask, render_template, url_for
import classification as cl

app = Flask(__name__)

range = cl.bpm_range


@app.route('/')
def helloWorld():
    return render_template('index.html', name=range)

if __name__ =='__main__':
    app.run(debug=True)