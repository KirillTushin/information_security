from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import os
from ML.Machine_Learning_part.malware_cheker import predict_file

UPLOAD_FOLDER = '/home/kirill/Documents/Data Science/MIPT/information_security/data_upload/'
MODEL_PATH = '/home/kirill/Documents/Data Science/MIPT/information_security/app/ML/Machine_Learning_part/best_classifier/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            file = request.files['file']
        except:
            return render_template('index.html')
        if file:
            filename = file.filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            score = predict_file(UPLOAD_FOLDER + filename, MODEL_PATH)

            return render_template('res.html', clas = score[1], text = score[0])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
