# List

N = int(input())

arr = []

for i in range(N):
    x = input()
    query_data = x.split()
    if query_data[0] == 'insert':
        arr.insert(int(query_data[1]), int(query_data[2]))
    elif query_data[0] == 'remove':
        arr.remove(int(query_data[1]))
    elif query_data[0] == 'sort':
        arr.sort()
    elif query_data[0] == 'append':
        arr.append(int(query_data[1]))
    elif query_data[0] == 'pop':
        arr.pop()
    elif query_data[0] == 'reverse':
        arr.reverse()
    elif query_data[0] == 'print':
        print(arr)

# Tuple


