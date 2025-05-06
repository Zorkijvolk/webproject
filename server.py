from flask import Flask, render_template
from requests import get
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

server_address_map = 'https://static-maps.yandex.ru/v1?'
map_api_key = 'MAP_API_KEY'


@app.route("/")
def index():
    return render_template("index.html", title='Replicas')


@app.route("/Moscow")
def moscow():
    map_request = f"{server_address_map}bbox=36.803079,55.142226~37.967466,56.021286&apikey={map_api_key}"
    map_response = get(map_request)

    map_file = "moscow.png"
    with open(f'static/img/{map_file}', "wb") as file:
        file.write(map_response.content)
    return render_template("moscow.html", title='Moscow')


if __name__ == '__main__':
    app.run()
    if os.access("static/img/moscow.png", os.F_OK):
        os.remove('static/img/moscow.png')
