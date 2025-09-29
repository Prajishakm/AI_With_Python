import numpy as np
import matplotlib.pyplot as plt

n_values = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for n in n_values:
    dice1 = np.random.randint(1, 7, n)
    dice2 = np.random.randint(1, 7, n)
    sums = dice1 + dice2

plt.hist(sums, bins=range(2, 14), density=True, alpha=0.7, color="blue", edgecolor="black")

plt.xlabel("Sum of Two Dice")

plt.show()