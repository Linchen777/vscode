import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def function(i):
    line.set_ydata(np.sin(x + i / 30))
    return line,


def ini_function():
    line.set_ydata(np.sin(x))
    return line,


ani = matplotlib.animation.FuncAnimation(fig=fig, func=function, frames=100, init_func=ini_function, interval=20,
                                         blit=False, )
plt.show()
