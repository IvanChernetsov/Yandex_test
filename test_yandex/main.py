from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET', 'PUT'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Ообор астронавтов</title>
                          </head>
                          <body>
                            <h1 class='center'>Загрузка фотографии</h1>
                            <h2 class='center'>Для участия в миссии</h2>
                            <div class='s center'>
                                <form method="post" enctype="multipart/form-data" class='bgp'>
                                <div class="form-group center gl">
                                        <label for="photo">Выберите фото </label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class='center gl'>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Ообор астронавтов</title>
                          </head>
                          <body>
                            <h1 class='center'>Загрузка фотографии</h1>
                            <h2 class='center'>Для участия в миссии</h2>
                            <div class='s center'>
                                <form method="post" enctype="multipart/form-data" class='bgp'>
                                <div class="form-group center gl">
                                        <label for="photo">Выберите фото </label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class='center'>
                                        <img src="{url_for('static', filename='img/foto.png')}" alt="здесь должна была быть картинка, но не нашлась">
                                    </div>
                                    <div class='center'>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')