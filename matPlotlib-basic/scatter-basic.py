import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')
x = [3, 6, 7, 9, 10]
y = [5, 10, 25, 3, 1]

plt.title("Test Scatter")
plt.xlabel("Test X Label")
plt.ylabel("Test Y Label")

plt.scatter(x, y)

plt.show()
