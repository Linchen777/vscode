import matplotlib.pyplot as plt
import numpy as np


def f(A, B):
    return (1 - A / 2 + A ** 5 + B ** 3) * np.exp(-A ** 2 - B ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.jet)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=0.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
