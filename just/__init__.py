from __future__ import absolute_import

from flask import Flask

import os

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.abspath('uploads')
EXAMPLES_NOTARY = os.path.abspath('examples/notary_examples')
EXAMPLES_RECLAMATION = os.path.abspath('examples/reclamation_examples')
DOWNLOAD_NOTARY = os.path.abspath('downloads/notary_downloads')
DOWNLOAD_RECLAMATION = os.path.abspath('downloads/reclamation_downloads')
TEXT_ROOT =  os.path.abspath('uploads')
app = Flask(__name__, static_folder='static')
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXAMPLES_NOTARY'] = EXAMPLES_NOTARY
app.config['DOWNLOAD_NOTARY'] = DOWNLOAD_NOTARY
app.config['EXAMPLES_RECLAMATION'] = EXAMPLES_RECLAMATION
app.config['DOWNLOAD_RECLAMATION'] = DOWNLOAD_RECLAMATION
app.config['TEXT_ROOT'] = TEXT_ROOT
import just.views
