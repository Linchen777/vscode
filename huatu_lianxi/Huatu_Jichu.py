import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(1)
line2, = plt.plot(x, y2, label='up')  # 要加逗号
line1, = plt.plot(x, y1, 'red', linewidth=1.0, linestyle='--', label='down')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am X')
plt.ylabel('I am Y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, 0, 1.8, 2], [r'$really\ bad$', r'$bad\theta$', r'$normal$', r'$good$', r'$really\ good$'])

# gca = 'get current axis'
# ax.spines:上下左右的边框
ax = plt.gca()
ax.spines['right'].set_color('none')  # 设置右边和顶边为无色
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 用底边作为x轴，用左边作为y轴
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))  # 横坐标移动到y=-1处
ax.spines['left'].set_position(('data', 0))  # 纵坐标移动到x=0处
# data 可以换成 outward 或者 axes

# 图例 legend
plt.legend(handles=[line1, line2], labels=['aaa', 'bbb'], loc='best')


plt.show()
