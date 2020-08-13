import matplotlib.pyplot as plt
import numpy as np
# 左右两边双y坐标轴，共享x坐标轴
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # ax2 是把 ax1 左右翻转，共享x轴
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')

plt.show()