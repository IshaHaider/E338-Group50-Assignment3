import sys

def print_capacity_change(lst, prev_size):
    print(f"List capacity changed to {len(lst)} element(s) (total size: from {prev_size} bytes -> {sys.getsizeof(lst)} bytes)")

lst = []
prev_size = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    if prev_size is None or prev_size != sys.getsizeof(lst):
        print_capacity_change(lst, prev_size)
        prev_size = sys.getsizeof(lst)
