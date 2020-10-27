import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')
numbers = [1, 20, 15, 23, 69, 87, 10, 23, 56, 4, 79, 52, 32, 14,
           16, 96, 20, 23, 51, 48, 75, 96, 25, 63, 98, 74, 52, 14, 23, 69]
jumps = [0, 15, 30, 45, 60, 75, 90, 105]

plt.title("Test Histrogram")
plt.xlabel("Test X Label")
plt.ylabel("Test Y Label")

plt.hist(numbers, jumps, histtype="step")

plt.show()
