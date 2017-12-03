#!/usr/bin/env python3
r = [1, 2, 3, 4, 5]

# r[start:end]  => start -> end-1
print(r[0:1])  # [1]

# r[start:] => start -> rest of the list
print(r[0:])  # [1,2,3,4,5]

# r[:end] => 0 -> end-1
print(r[:4])  # [1,2,3,4] 0~3

# r[:] => a copy of the whole list
print(r[:])

# r[start:end:step] => start -> end-1 -> jump with step
print(r[0:4:2])

# r[-1] => last item in list
print(r[-1])  # 5

# r[-2:] => last two items in list Means starts from -2 to end
print(r[-2:])  # [4,5]

# r[:-2] Everything except last two items
print(r[:-2])  # [1,2,3]

# r[::-1] reverse a list
print(r[::-1])  # [5,4,3,2,1]
# Note python do not have built in reverse function
