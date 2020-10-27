import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

x = [2, 4, 6]
y = [3, 6, 9]

x2 = [4, 8, 12]
y2 = [5, 10, 15]

x3 = [6, 12, 18]
y3 = [12, 24, 36]

plt.bar(x, y)
plt.bar(x2, y2)
plt.bar(x3, y3)

plt.title("Test")
plt.xlabel("Test x values")
plt.ylabel("Test y values")
plt.show()


print("----------------------------")
