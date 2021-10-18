import random
import time

class Algorithm():
    def __init__ (self, name):
        self.array = random.sample(range(512), 512)

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)
    
    def run(self):
        self.start_time = time.time()
        self.algorithm
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed



class bubble_sort(Algorithm):
    def __init__(self, name):
        super().__init__(name)

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array - 1 - i)):
                if j > j+1:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                self.update_display(self.array[j], self.array[j+1])

class insertion_sort(Algorithm):
    def __init__(self, name):
        super().__init__(name)

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx - 1] > cursor:
                self.array[idx] = self.array[idx - 1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])

def quick_sort(arr, low, high):
    if low >= 0 and high >= 0 and low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]        