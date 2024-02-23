train_data = [[0, 1], [1, 1]]
o = [0, 1]
w1 = 0.35
w2 = 0.81
ni = 0.25
epochs = 1

for _ in range(epochs):
    for x, target in zip(train_data, o):
        inp1 = x[0] * w1
        inp2 = x[1] * w2
        output = inp1 + inp2
        error = target - output
        chw1 = ni * x[0] * error
        chw2 = ni * x[1] * error
        w1 += chw1
        w2 += chw2
