import sys

prev_capacity = 0
for i in range(64):
    lst = list(range(i))
    if lst:
        cur_capacity = sys.getsizeof(lst) - sys.getsizeof(lst[0]) * i
        if cur_capacity != prev_capacity:
            print(f"List capacity changed from {prev_capacity} to {cur_capacity} at length {i}")
            prev_capacity = cur_capacity
