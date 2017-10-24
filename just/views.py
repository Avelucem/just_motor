from just import app
from io import StringIO
import os
from functools import wraps
import zipfile

from flask import Flask, request, redirect, url_for, flash, send_from_directory, render_template
from werkzeug.utils import secure_filename
import json

from just.court_2610.nice_look import data, columns

ALLOWED_EXTENSIONS = set(['xls'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
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

@app.route('/download_notary_file/<filename>')
def download_notary_file(filename):
    zipfile.ZipFile(os.path.abspath('downloads/notary_downloads/notary_app.zip'), mode = 'w')
    from just.notary.notary_app import notary_app
    notary_app()
    return send_from_directory(app.config['DOWNLOAD_NOTARY'],
                               filename)

@app.route('/download_reclamation_file/<filename>')
def download_reclamation_file(filename):
    zipfile.ZipFile(os.path.abspath('downloads/reclamation_downloads/reclamation_app.zip'), mode = 'w')
    from just.reclamation.reclamation_app import reclamation_app
    reclamation_app()
    return send_from_directory(app.config['DOWNLOAD_RECLAMATION'],
                               filename)

@app.route('/notary_examples/<filename>', methods=['GET', 'POST'])
def download_exapmles_notary(filename):
    return send_from_directory(app.config['EXAMPLES_NOTARY'],
                               filename)

@app.route('/reclamation_examples/<filename>', methods=['GET', 'POST'])
def download_exapmles_reclamation(filename):
    return send_from_directory(app.config['EXAMPLES_RECLAMATION'],
                               filename)

@app.route('/court_2610/', methods=['GET', 'POST'])
def index():
    return render_template("court_2610.html",
      data=data,
      columns=columns,
      title='Результаты автоматического распределения в Шевченковском районном суде города Киева')

@app.route('/court_2610/rewind/', methods=['GET', 'POST'])
def index_rewind():
    from just.court_2610.court_2610 import court_2610
    court_2610()
    return render_template("court_2610.html")
