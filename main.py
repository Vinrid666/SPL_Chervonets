import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
x = x[x != 0]  # виключаємо нуль, щоб уникнути ділення на 0
y = (1 / x) * np.sin(5 * x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue')
plt.title('Графік функції Y(x) = (1/x) * sin(5x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

plt.savefig('images/graph.png', dpi=300)
plt.show()
