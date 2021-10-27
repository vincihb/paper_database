import numpy as np


class Linear:
    def __init__(self, x, y):
        cov = 1 / (len(x) - 1) * np.sum([(x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(0, len(x))])
        cor = np.sum([(x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(0, len(x))]) \
              / (np.sqrt(np.sum([(x[i] - np.mean(x)) ** 2 for i in range(0, len(x))]))
                 * np.sqrt(np.sum([(y[i] - np.mean(y)) ** 2 for i in range(0, len(x))])))
        print(cor)
        self.b = np.mean(y) - cov / np.var(x) * np.mean(x)
        self.m = cov / np.var(x)
        num_points = 1000
        self.x_array = [a * ((int(max(x) + 1) - int(min(x) - 1)) / num_points) + int(min(x) - 1) for a in
                        range(0, num_points, 1)]
        self.y_hat = [self.m * x_val + self.b for x_val in self.x_array]
        self.r = 1 - np.sum([np.power(self.m * x[index] + self.b - y[index], 2) for index in range(0, len(x))]) \
                / np.sum([(y[i] - np.mean(y)) ** 2 for i in range(0, len(x))])

    def get_m_b(self):
        return self.m, self.b

    def get_all_data(self):
        return self.m, self.b, self.r, self.x_array, self.y_hat
