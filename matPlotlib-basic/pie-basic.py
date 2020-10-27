import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')
food = ["pizza", "ice cream", "burgers"]
sales = [20, 10, 30]
color = ["red", "blue", "yellow"]

plt.title("Test Pie")

plt.pie(sales, labels=food, colors=color)

plt.show()
