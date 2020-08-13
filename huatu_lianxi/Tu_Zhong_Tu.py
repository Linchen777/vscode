import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 主图
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('TOTAL')

# 子图1 左上角
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'b')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('INSIDE 1')

# 子图2 右下角
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('INSIDE 2')

plt.show()
