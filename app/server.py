from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import os
from ML.Machine_Learning_part.malware_cheker import predict_file

UPLOAD_FOLDER = '/home/kirill/Documents/Data Science/MIPT/information_security/data_upload/'
MODEL_PATH = '/home/kirill/Documents/Data Science/MIPT/information_security/ML/Machine_Learning_part/best_classifier/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    score = -1
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            score = predict_file(UPLOAD_FOLDER + filename, MODEL_PATH)
            return render_template('index_score.html', filename=filename, score=score)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
