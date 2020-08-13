import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)  # 均匀分布
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')  # 向上画柱状图
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')  # 向下画柱状图

# 设置柱子上面的数字
for x, y in zip(X, Y1):  # zip:把X,Y1,分别传入x,y
    # ha: horizontal alignment 水平对齐方式  va: vertical alignment
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='bottom', fontsize=16)

for x, y in zip(X, Y2):  # zip:把X,Y1,分别传入x,y
    # ha: horizontal alignment 水平对齐方式  va: vertical alignment
    plt.text(x, -y-0.05, '-%.2f' % y, ha='center', va='top', fontsize=16)

plt.xlim(-0.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
