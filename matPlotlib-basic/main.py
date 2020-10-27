import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')
print(style.available)

plt.plot([1, 3, 5, 10], [5, 18, 25, 125])
plt.show()

x = [2, 4, 8]
y = [4, 8, 24]

x2 = [3, 6, 9]
y2 = [10, 15, 30]

plt.plot(x, y)
plt.plot(x2, y2)
plt.show()

plt.plot(x, y)
plt.plot(x2, y2)
plt.title("Test")
plt.xlabel("Test x values")
plt.ylabel("Test y values")
plt.show()


print("----------------------------")
