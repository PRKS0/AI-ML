import numpy as np
import matplotlib.pyplot as plt
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

# print("First 3 restaurant: \n", sales_data[:3])

# total sales per year
data = sales_data[:, 1:]
# print("sales per year: \n", np.sum(data, axis=0))
# print("\n sales per restaurant: \n", np.sum(data, axis=1))
# print("\n Minumum Sale per restaurant: \n", np.min(data, axis=1))
# print("\n Average Sale per restaurant: \n", np.mean(data, axis=1))


cumsum = np.cumsum(data, axis=1)
# print(cumsum)

plt.figure(figsize=(8, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average cumulative sales accross all resutrant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
# plt.show()


vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

print("Vector addition: \n", vector1 + vector2)
print("Vector multiplication: \n", vector1 * vector2)
print("Dot product: \n", np.dot(vector1, vector2))
# dot product: a1.b1 + a2.b2 + a3.b3

import sys
print(sys.executable)