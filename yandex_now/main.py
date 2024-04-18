from flask import Flask, url_for, request
import json
import random

app = Flask(__name__)



@app.route('/member')
def sample_file_upload():
  with open("templates/index.json", "r", encoding='utf-8') as f:
      templates = json.load(f)
  mn = []
  for i in templates.items():
    mn.append(i)
  rn = mn[random.randint(0, 2)]
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
                            <div class="bgp">
                              <div class="container" style="display: flex; justify-content: space-between; align-items: center;">
                                <h1 class="bgp">Миссия Колонизация Марса</h1>
                                <div>Mars One</div>
                              </div>
                            </div>
                            <div class='container'>
                              <div class='text-secondary'>И на Марсе будут яблони цвести!</div>
                              <div class='center'>
                                <h2>{rn[1][0]}</h2>
                              </div>
                              <div class="w-100"></div>
                              <div class='center'>
                                <img src='{rn[1][2]}'>
                              </div>
                              <div class="w-100"></div>
                              <div class='center'>
                                <h6>{rn[1][1]}</h6>
                              </div>
                              <div class="w-100"></div>
                            </div>
                          </body>
                        </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')