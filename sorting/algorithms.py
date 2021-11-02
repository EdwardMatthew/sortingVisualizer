from abc import abstractproperty
import random
import time

class Algorithm():
    def __init__(self, name):
        self.name = name
        self.array = random.sample(range(512), 512)

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("Bubble Sort")
    
    def algorithm(self):
        for i in range(0, len(self.array) - 1):
            for j in range(len(self.array)- 1 - i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx - 1] > cursor:
                self.array[idx] = self.array[idx - 1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")
    
    def algorithm(self, arr=[], start=0, end=0):
        if arr == []:
            arr = self.array
            end = len(arr) - 1
        if start < end:
            pivot = self.partition(arr, start, end)
            self.algorithm(arr, start, pivot - 1)
            self.algorithm(arr, pivot + 1, end)

    def partition(self, arr, start, end):
        n = arr[end]
        i = start - 1
        for j in range(start, end+1, 1):
            if arr[j] <= n:
                i += 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    self.update_display(arr[i], arr[j])
        return i

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")
    
    def algorithm(self):
        for i in range(len(self.array)-1):
            min = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min]: 
                    min = j
            self.array[i], self.array[min] = self.array[min], self.array[i] 
            self.update_display(self.array[i], self.array[j])     