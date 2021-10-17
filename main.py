import numpy as np
import scipy as sp
import time
import sorting.sorting as s

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# configuring runtime parameters
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16

N = 1000
arr = np.round(np.linspace(0, 1000, N), 0)
np.random.shuffle(arr)

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1), arr, align='edge')

t0 = time.perf_counter()
s.selection_sort(arr)
dt = time.perf_counter() - t0

print(f"Array sorted in {dt*1E3:.1f} ms")

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1), arr, align='edge')

plt.show()