import math

from flask import Flask, render_template

app = Flask(__name__)


def draw_sin(matrica):
    for x in range(50):
        for y in range(24 - int(math.sin(x / 5) * 15), 50):
            matrica[y][x] = 'x'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display')
def display_data():
    display = ""
    matrix = [['o'] * 50 for _ in range(50)]
    draw_sin(matrix)
    for x in matrix:
        for y in x:
            display += str(y)
        display += '<br>'
    return render_template('display.html', display=display)


if __name__ == '__main__':
    app.run(port=5001)
