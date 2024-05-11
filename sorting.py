import time
import random
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def compare_sorting_algorithms(arr):
    start_time = time.time()
    selection_sort(arr.copy())
    selection_time = time.time() - start_time

    start_time = time.time()
    bubble_sort(arr.copy())
    bubble_time = time.time() - start_time

    start_time = time.time()
    quick_sort(arr.copy())
    quick_time = time.time() - start_time

    start_time = time.time()
    merge_sort(arr.copy())
    merge_time = time.time() - start_time

    return selection_time, bubble_time, quick_time, merge_time

def plot_execution_times(times, labels, title):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, times, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Execution Time (s)')
    plt.title(title)
    plt.show()


# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
arr2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr3 = [5, 2, 8, 1, 9, 3, 7, 6, 4, 10]
arr4 = [random.randint(1, 1000) for _ in range(1000)]

labels = ['Selection Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort']

times1 = compare_sorting_algorithms(arr1)
plot_execution_times(times1, labels, 'Execution Times for Array 1')
print("Comparison of Execution Times for Array 1:")
print("Selection Sort Time:", times1[0])
print("Bubble Sort Time:", times1[1])
print("Quick Sort Time:", times1[2])
print("Merge Sort Time:", times1[3])

times2 = compare_sorting_algorithms(arr2)
plot_execution_times(times2, labels, 'Execution Times for Array 2')
print("Comparison of Execution Times for Array 2:")
print("Selection Sort Time:", times2[0])
print("Bubble Sort Time:", times2[1])
print("Quick Sort Time:", times2[2])
print("Merge Sort Time:", times2[3])

times3 = compare_sorting_algorithms(arr3)
plot_execution_times(times3, labels, 'Execution Times for Array 3')
print("Comparison of Execution Times for Array 3:")
print("Selection Sort Time:", times3[0])
print("Bubble Sort Time:", times3[1])
print("Quick Sort Time:", times3[2])
print("Merge Sort Time:", times3[3])

times4 = compare_sorting_algorithms(arr4)
plot_execution_times(times4, labels, 'Execution Times for Array 4')
print("Comparison of Execution Times for Array 4:")
print("Selection Sort Time:", times4[0])
print("Bubble Sort Time:", times4[1])
print("Quick Sort Time:", times4[2])
print("Merge Sort Time:", times4[3])