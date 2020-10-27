import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset('flights')
print(database)

sb.catplot(x='month', y='passengers', data=database)
plt.show()

sb.catplot(x='month', y='passengers', data=database, kind='violin')
plt.show()

sb.catplot(x='month', y='passengers', data=database, kind='box')
plt.show()
