# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, flash,session
from flask_cors import CORS
import sys
from imlucky import load

app = Flask(__name__, template_folder='../templates', static_folder='../data')

#enable CORS
CORS(app)

#test

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong lol')
##import requests
##
##@app.route('/', defaults={'path': ''})
##@app.route('/<path:path>')
##def catch_all(path):
##    if app.debug:
##        return requests.get('http://localhost:8080/{}'.format(path)).text
##    return render_template("index.html")

from flask import Flask, Response, request, render_template, jsonify
from flask_cors import cross_origin
from time import perf_counter
import os
import base64
import random # Avoid * imports as they add a lot of unkwnown namespaces to your file
import json
@app.route('/api/upload', methods=['GET','POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload_me():
    if request.method == 'GET':
        """ Show saved image """
        if os.path.exists('file.img'):
            with open('file.img', 'r') as rf:
                data = rf.read()
                mimetype, image_string = data.split(';base64,')
                image_bytes = image_string.encode('utf-8')
                return Response(base64.decodebytes(image_bytes), mimetype=mimetype)

    if request.method == 'POST':
        """ Receive base 64 encoded image """
        start = perf_counter()
        print('Request received')
        request_data = json.loads(request.get_data())
        data = request_data['data'][5:]

##        with open('file.img', 'w') as wf:
##            wf.write(data)
        file = data
        # if user does not select file, browser also
        # submit a empty part without filename
       
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('Saved in file.')
        print('Time elapsed: {}'.format(perf_counter() - start))
        return Response(status=200)

    return render_template('about.html')


import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '../datas'
ALLOWED_EXTENSIONS = set(['jpg'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/about', methods=['GET', 'POST'])
def upload_file():
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
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#  end test

def get_pictures_repo():
   import dummy_database
   return dummy_database.pictures_repo


imlucky = load(sys.argv[1], get_pictures_repo())


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def imlucky_action():
    files = imlucky()
    print('asdas',files)
    import csv
    _files = []
    with open('../csv/female/Database_Dress.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for i in files:
                # print(i[0][0].replace('data/', ''))
                if str(row[1]) in i[0][0].replace('data/', ''):
                    print(row[1], row[4], row[3],row[2])
                    _files.append( [[i[0][0], i[1]], i[1], row[4], row[3],row[2]])

    print('ghjgjh',_files)

    return render_template('index.html', files=_files )



app.secret_key = "super secret key"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
