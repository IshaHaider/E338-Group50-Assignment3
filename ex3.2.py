import json
import matplotlib.pyplot as plt
import time

def load_data():
    with open('ex2data.json') as f:
        data = json.load(f)
        return data

def load_tasks():
    with open('ex2tasks.json') as f:
        tasks = json.load(f)
        return tasks

def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

def find_best_midpoint(arr, target):
    start = 0
    end = len(arr) - 1
    best_mid = (start + end) // 2
    best_time = float('inf')
    for i in range(start, end+1):
        mid = i
        t0 = time.time()
        binary_search(arr, target, start, mid)
        t1 = time.time()
        elapsed = t1 - t0
        if elapsed < best_time:
            best_time = elapsed
            best_mid = mid
    return best_mid

if __name__ == '__main__':
    data = load_data()
    tasks = load_tasks()
    best_mids = []
    for task in tasks:
        best_mid = find_best_midpoint(data, task)
        best_mids.append(best_mid)
        print(f"Task {task}: best midpoint = {best_mid}")

    plt.scatter(tasks, best_mids)
    plt.xlabel('Search task')
    plt.ylabel('Best midpoint')
    plt.title('Best midpoint for each search task')
    plt.show()
