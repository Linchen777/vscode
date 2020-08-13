from scipy.integrate import odeint
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def runge_kutta(y, x, dx, f):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """
    k1 = dx * f(y, x)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.


def lorenz(w, t, p, r, b):
    # 给出位置矢量w，和三个参数p, r, b计算出
    # dx/dt, dy/dt, dz/dt的值
    x, y, z = w
    # 直接与lorenz的计算公式对应
    return np.array([p * (y - x), x * (r - z) - y, x * y - b * z])


# t = 0.
x = 0.
y = 1.
z = 0.
# dt = .1
dx = .1
xs, ys, zs = [], [], []

while x <= 10:
    y = runge_kutta(y, x, dx, lorenz)

    x += dx
    ys.append(y)
    xs.append(x)

exact = [(t ** 2 + 4) ** 2 / 16. for t in ts]
plt.plot(ts, ys, label='runge_kutta')
plt.plot(ts, exact, label='exact')
plt.legend()
plt.show()
