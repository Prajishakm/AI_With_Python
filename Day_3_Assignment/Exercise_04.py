import numpy as np

A = np.array([[0, 1, 4],
              [1, 2, 3],
              [5, 6, 0]])

print("Original Matrix A:")
print(A)
print()

A_inv = np.linalg.inv(A)
print("Inverse Matrix A⁻¹:")
print(A_inv)
print()

AA_inv = np.dot(A, A_inv)
print("A × A⁻¹ (should be like the number 1 for matrices):")
print(AA_inv)
print()

AinvA = np.dot(A_inv, A)
print("A⁻¹ × A (should be like the number 1 for matrices):")
print(AinvA)
print()