import sys
import json
import time
import matplotlib.pyplot as plt
import threading

threading.stack_size(33554432)
sys.setrecursionlimit(20000)

with open('ex2.json', 'r') as f:
    inputs = [json.load(f)]

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

times = []
for arr in inputs:
    start_time = time.time()
    func1(arr, 0, len(arr)-1)
    end_time = time.time()
    time_taken = end_time - start_time
    times.append(time_taken)

plt.plot([len(arr) for arr in inputs], times, marker='o')
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort performance')
plt.show()
