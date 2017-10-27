from __future__ import absolute_import
import os
from flask import Flask


UPLOAD_FOLDER = os.path.abspath('uploads')
EXAMPLES = os.path.abspath('examples')
DOWNLOAD_NOTARY = os.path.abspath('downloads/notary_downloads')
DOWNLOAD_RECLAMATION = os.path.abspath('downloads/reclamation_downloads')


app = Flask(__name__, static_folder='static')
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXAMPLES'] = EXAMPLES
app.config['DOWNLOAD_NOTARY'] = DOWNLOAD_NOTARY
app.config['DOWNLOAD_RECLAMATION'] = DOWNLOAD_RECLAMATION


import just.views
