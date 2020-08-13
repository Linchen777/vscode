import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
# X,Y value
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2+Y**2)
# height value
Z = np.sin(R)
# 画图 彩虹色的3D图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# rstride 和 cstride 是单位格子的跨度，越小越密集，越大越稀疏
ax.contourf(X, Y, Z, zdir='z', offset=-4, cmap='rainbow')  # zdir:从哪个方向压到平面上。'x' 'y' 'z'
ax.set_zlim(-2, 2)  # 固定等高线图高度范围

plt.show()

