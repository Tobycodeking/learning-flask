from flask import *
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

app = Flask(__name__)
app.config['upload_folder'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10* 1024 * 1024

@app.route('/')
def index():
    return '<p>Click here to <a href="upload" target="_blank">upload a profile picture</a>'
    
@app.route('/upload')
def upload():       
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST', 'GET'])
def uploader():
    if request.method == 'POST':

        try:

            file = request.files['profilePicture']

            if file:
                file.save(os.path.join(

                    app.config['upload_folder'], secure_filename(file.filename)
                    
                    ))

                return render_template('uploaded.html')

        except RequestEntityTooLarge:

            return 'file size is more than 10MB limit \
            <a href="upload" target="_blank">try again</a>'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)