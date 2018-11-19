from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import os
import random

UPLOAD_FOLDER = '/home/kirill/Documents/Data Science/MIPT/information_security/data_upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


Bootstrap(app)


def return_score(file):
    return random.randint(0, 100)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    score = -1
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            score = return_score(filename)
            return render_template('index_score.html', filename=filename, score=score)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
