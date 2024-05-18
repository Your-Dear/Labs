import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

# №1

size = 1000000
list1 = [np.random.random() for _ in range(size)]
list2 = [np.random.random() for _ in range(size)]

start_time = time.perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_time = time.perf_counter()
print(f"Время выполнения с использованием списков: {end_time - start_time} секунд")

array1 = np.array(list1)
array2 = np.array(list2)

start_time = time.perf_counter()
result_array = np.multiply(array1, array2)
end_time = time.perf_counter()
print(f"Время выполнения с использованием NumPy: {end_time - start_time} секунд")

# №2
data = pd.read_csv('data1.csv', encoding='cp1251', delimiter=";")
x = data.iloc[:, 3]  
y = data.iloc[:, 17] 

plt.figure(figsize=(12, 6))
plt.plot(x, label='Column 4')
plt.plot(y, label='Column 18')
plt.title('Comparison of Column 4 and Column 18')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()

# Построение графика корреляции
plt.figure(figsize=(6, 6))
plt.scatter(x, y)
plt.title('Correlation between Column 4 and Column 18')
plt.xlabel('Column 4')
plt.ylabel('Column 18')
plt.show()

# №3
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y = np.cos(x)
z = np.sin(x)
# Построение трехмерного графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title('3D Plot for the Given Formula')
ax.set_xlabel('X')
ax.set_ylabel('Y (cos(x))')
ax.set_zlabel('Z (sin(x))')
plt.show()

#Доп Зад
def sin_wave(x):
    return np.sin(x)


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(sin_wave(frame))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)


ani.save('sin_wave_animation.gif', writer='pillow', fps=30)
plt.show()