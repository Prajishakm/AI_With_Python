import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 200)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.plot(x, y1, 'r-', label="y = 2x + 1")
plt.plot(x, y2, 'b--', label="y = 2x + 2")
plt.plot(x, y3, 'g:', label="y = 2x + 3")

plt.title("y = 2x + c")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid(True)
plt.legend()

plt.show()