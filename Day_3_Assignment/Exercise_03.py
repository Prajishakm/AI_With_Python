import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('weight-height.csv', delimiter=',', skip_header=1, usecols=(1, 2))

length = data[:, 0]
weight = data[:, 1]

length_cm = length * 2.54

weight_kg = weight * 0.453592

mean_length = np.mean(length_cm)
mean_weight = np.mean(weight_kg)

print(f"Mean length: {mean_length:.2f} cm")
print(f"Mean weight: {mean_weight:.2f} kg")

plt.figure(figsize=(10, 6))
plt.hist(length_cm, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Student Lengths')
plt.grid(True, alpha=0.3)

plt.axvline(mean_length, color='brown', linestyle='--', linewidth=2,
            label=f'Mean: {mean_length:.2f} cm')
plt.legend()

plt.show()