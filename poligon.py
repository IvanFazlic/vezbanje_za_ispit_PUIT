import math

from flask import Flask, render_template

app = Flask(__name__)


def is_inside_shape(point, shape):
    x, y = point
    n = len(shape)
    inside = False

    p1x, p1y = shape[0]
    for i in range(n + 1):
        p2x, p2y = shape[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# Example usage:
shape = [[0, 1], [4, 4], [2, 2]]
point = [0, 1]
print(is_inside_shape(point, shape))


def draw_a_line(matrix, firstInput, secondInput):
    x1, y1 = firstInput
    x2, y2 = secondInput
    deltaX = abs(x2 - x1)
    deltaY = abs(y2 - y1)
    steps = max(deltaX, deltaY)
    if steps == 0:
        return  # Points are the same, no need to draw a line
    xinc = (x2 - x1) / steps
    yinc = (y2 - y1) / steps
    for i in range(steps):
        matrix[int(round(x1))][int(round(y1))] = 'x'
        x1 += xinc
        y1 += yinc


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display_poligon/<int:number>')
def display_poligon(number):
    display = ""
    dot_array = []
    matrix = [['o'] * 50 for _ in range(50)]
    for angle in range(0, 360, int(360 / number)):
        x = int(24 * math.sin(math.radians(angle))) + 24
        y = int(24 * math.cos(math.radians(angle))) + 24
        dot_array.append([x, y])
    # for x in range(len(dot_array)):
    #     draw_a_line(matrix, dot_array[x], dot_array[(x + 1) % len(dot_array)])
    for x in range(50):
        for y in range(50):
            if is_inside_shape([x, y], dot_array):
                matrix[x][y] = 'x'
    for row in matrix:
        for element in row:
            display += str(element)
        display += '<br>'
    print(dot_array)
    return render_template('display.html', display=display)


if __name__ == '__main__':
    app.run(port=5001)
