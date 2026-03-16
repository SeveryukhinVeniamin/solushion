from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return f"""<!doctype html>
        <html>
            <head>
                <title>Марс</title>
            </head>
            
            <body>
                <h1>И на Марсе будут яблони цвести!</h1>
            </body>
        </html>"""


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
        <html>
            <head>
                <title>Марс</title>
            </head>
            <body>
                <h1>Человечество вырастает из детства.</h1>
                <h1>Человечеству мала одна планета.</h1>
                <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                <h1>И начнем с Марса!</h1>
                <h1>Присоединяйся!</h1>
            </body>
        </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
            <html>
                <head>
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/image_mars.jpg">
                    <h3>Вот она какая, красная плвнета.</h3>

                </body>
            </html>"""

@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/image_mars.jpg">
                        
                        <div class="alert alert-primary" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-danger" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Присоединяйся!
                        </div>

                    </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Мое предложение, {planet_name}!</h1>

                        <div class="alert alert-primary" role="alert">
                          Эта планета близка к Земле;
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-success" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-danger" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Наконец она просто красива!
                        </div>

                    </body>
                </html>"""
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Results of custing:</h1>

                        <div class="alert alert-primary" role="alert">
                          Pretendent {nickname}
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Your reyting after {level} level
                        </div>
                        <div class="alert alert-success" role="alert">
                          {rating}
                        </div>

                    </body>
                </html>"""

if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
