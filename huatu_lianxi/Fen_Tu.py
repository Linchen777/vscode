import matplotlib.pyplot as plt
plt.figure()
# 第一张图独占第一行，后三张图分占第二行
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 2])

plt.show()