import math

inp = [[0, 1], [1, 1]]
o = [0, 1]
epochs = 10
ni = 0.25
w1_wm1 = 0.62
w2_wm1 = 0.42
w3_wm1 = 0.55
w4_wm1 = -0.17
w1_wm2 = 0.35
w2_wm2 = 0.81

for _ in range(epochs):
    for x, target in zip(inp, o):
        inp1 = x[0] * w1_wm1 + x[1] * w3_wm1
        inp2 = x[0] * w2_wm1 + x[1] * w4_wm1
        out1 = 1 / (1 + math.exp(-inp1))
        out2 = 1 / (1 + math.exp(-inp2))
        inputOfOutNeural = out1 * w1_wm2 + out2 * w2_wm2
        output = 1 / (1 + math.exp(-inputOfOutNeural))
        error = target - output
        chw1_wm2 = ni * error * out1 * output * (1 - output)
        chw2_wm2 = ni * error * out2 * output * (1 - output)
        w1_wm2 = w1_wm2 + chw1_wm2
        w2_wm2 = w2_wm2 + chw2_wm2
        chw1_wm1 = ni * error * x[0] * out1 * (1 - out1)
        chw2_wm1 = ni * error * x[0] * out2 * (1 - out2)
        chw3_wm1 = ni * error * x[1] * out1 * (1 - out1)
        chw4_wm1 = ni * error * x[1] * out2 * (1 - out2)
        w1_wm1 = w1_wm1 + chw1_wm1
        w2_wm1 = w2_wm1 + chw2_wm1
        w3_wm1 = w3_wm1 + chw3_wm1
        w4_wm1 = w4_wm1 + chw4_wm1
        print(w1_wm1, w2_wm1, w3_wm1, w4_wm1)
