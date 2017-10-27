from just import app

import os

import zipfile

from flask import Flask, request, redirect, url_for, flash, send_from_directory, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['xls', 'txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index_page.html')


@app.route('/notary', methods=['GET', 'POST'])
def upload_file_notary():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_notary_file', filename='notary_app.zip'))
    return render_template('notary.html')


@app.route('/reclamation', methods=['GET', 'POST'])
def upload_file_reclamation():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_reclamation_file', filename='reclamation_app.zip'))
    return render_template('reclamation.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/examples/<filename>', methods=['GET', 'POST'])
def download_exapmles(filename):
    return send_from_directory(app.config['EXAMPLES'],
                               filename)


@app.route('/download_notary_file/<filename>')
def download_notary_file(filename):
    zipfile.ZipFile(os.path.abspath('downloads/notary_downloads/notary_app.zip'), mode='w')
    from just.notary.notary_app import notary_app
    notary_app()
    return send_from_directory(app.config['DOWNLOAD_NOTARY'],
                               filename)


@app.route('/download_reclamation_file/<filename>')
def download_reclamation_file(filename):
    zipfile.ZipFile(os.path.abspath('downloads/reclamation_downloads/reclamation_app.zip'), mode='w')
    from just.reclamation.reclamation_app import reclamation_app
    reclamation_app()
    return send_from_directory(app.config['DOWNLOAD_RECLAMATION'],
                               filename)


@app.route('/court_2610/', methods=['GET', 'POST'])
def index_2610():
    from just.court_2610.nice_look import nice_look_data, columns
    return render_template("court_2610.html",
                           data=nice_look_data(),
                           columns=columns,
                           title='Результаты автоматического распределения в Шевченковском районном суде города Киева')


@app.route('/court_2606/', methods=['GET', 'POST'])
def index_2606():
    from just.court_2606.nice_look import nice_look_data, columns
    return render_template("court_2606.html",
                           data=nice_look_data(),
                           columns=columns,
                           title='Результаты автоматического распределения в Печерском районном суде города Киева')
