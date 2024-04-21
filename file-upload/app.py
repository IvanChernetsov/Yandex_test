# -*- coding: utf-8 -*-
from flask import Flask, request, render_template_string, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return render_template_string('<img src="/uploads/{{ filename }}">', filename=filename)
        return f'''
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Варианты выбора</title>
        </head>
        <body>
            <h1 class='center'>Пейзажи Марса</h1>
            <div class='center'>
                <div class="mb-3">
                    <form method=post enctype=multipart/form-data>
                        <input type=file name=file accept="image/*">
                        <input type=submit value=Upload>
                    </form>

                <div id="carouselExample" class="carousel slide www">
                    <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="{url_for('static', filename='img/slide_1.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_2.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_3.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_4.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        {render_template_string('<img class="d-block w-100" src="/uploads/{{ filename }}">', filename=filename)}
                    </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>
                </div>
            </div>
        </body>
    </html>'''
    return f'''
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Варианты выбора</title>
        </head>
        <body>
            <h1 class='center'>Пейзажи Марса</h1>
            <div class='center'>
                <div class="mb-3">
                    <form method=post enctype=multipart/form-data>
                        <input type=file name=file accept="image/*">
                        <input type=submit value=Upload>
                    </form>

                <div id="carouselExample" class="carousel slide www">
                    <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="{url_for('static', filename='img/slide_1.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_2.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_3.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/slide_4.jpg')}" class="d-block w-100" alt="...">
                    </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>
                </div>
            </div>
        </body>
    </html>'''

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(port=5000)
