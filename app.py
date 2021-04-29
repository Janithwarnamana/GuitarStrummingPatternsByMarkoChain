from flask import Flask, render_template, url_for, request

from bpm_classification import BpmClassifier
from strum_pattern_generator import StrumPatternGenerator
import os
import uuid
import json
import data_preprocessor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# range = cl.bpm_range
# pattern = data_preprocessor.path


@app.route('/')
def app_route():
    return render_template('index.html', name=range)


@app.route('/pattern', methods=['GET', 'POST'])
def generate_patter():
    if request.method == 'POST':
        json_request = request.get_json()
        pattern = StrumPatternGenerator.generate_pattern(json_request['song'], json_request['time_signature'])
        return json.dumps(pattern)
    return "Unsupported Request"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        # extension = os.path.splitext(file.filename)[1]
        # f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return json.dumps({'filename': file.filename})


if __name__ == '__main__':
    app.run(debug=True)
