

import numpy as np
import matplotlib.pyplot as plt

x_train = np.random.randn(10)
y_train = 2.5 * x_train + 0.5 * np.random.randn(x_train.shape[0])
w_0 = 1
learning_rate = 0.1
tolerance = 1e-4

w_trace = [w_0]

while True:
    w_old = w_trace[-1]
    w_new = w_old - learning_rate * (2 * (w_old * x_train - y_train) * x_train).mean()
    
    w_trace.append(w_new)

    if np.abs(w_new - w_old) < tolerance:
        break
plt.scatter(x_train, y_train)
plt.plot(np.linspace(-2.5, 2.5), w_trace[-1] * np.linspace(-2.5, 2.5))
plt.savefig("pltxxx.png")