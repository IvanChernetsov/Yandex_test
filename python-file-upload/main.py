from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
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
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
                              <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                              <title>Варианты выбора</title>
                            </head>
                          <body>
                            <h1 class='center'>Пейзажи Марса</h1>
                            <div class='center'>
                              <div class="mb-3">
                                <form method="post" enctype="multipart/form-data" class='bgp'>
                                  <div class="form-group center gl">
                                        <label for="photo">Выберите фото </label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class='center gl'>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
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
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
                              <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                              <title>Варианты выбора</title>
                            </head>
                          <body>
                            <h1 class='center'>Пейзажи Марса</h1>
                            <div class='center'>
                              <div class="mb-3">
                                <form method="post" enctype="multipart/form-data" class='bgp'>
                                  <div class="form-group center gl">
                                        <label for="photo">Выберите фото </label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class='center gl'>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')