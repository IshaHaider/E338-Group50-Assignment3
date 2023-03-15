import sys

def print_capacity_change(lst):
    print(f"Underlying list capacity changed to {len(lst)} element(s)")
    

lst = []
prev_size = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    if prev_size != sys.getsizeof(lst):
        print_capacity_change(lst)
        prev_size = sys.getsizeof(lst)
    
print_capacity_change(lst)
