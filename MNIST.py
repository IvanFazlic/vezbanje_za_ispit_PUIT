from tensorflow.keras.datasets import mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = np.reshape(x_train, (x_train.shape[0], -1))
x_train = x_train / 255.

x_test = np.reshape(x_test, (x_test.shape[0], -1))
x_test = x_test / 255.


