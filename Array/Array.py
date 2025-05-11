def insert(arr, n, pos, value):
    # Check if space available
    if n >= len(arr):
        print("Array full")
        return n
    
    # Shift elements to right
    for i in range(n, pos, -1):
        arr[i] = arr[i - 1]
    
    arr[pos] = value
    return n + 1  # new size


from array import array

arr = array('i', [10, 20, 30, 40, 0, 0])  # extra space
n = 4
n = insert(arr, n, 2, 25)  # Insert 25 at index 2

print("After Insert:")
for i in range(n):
    print(arr[i], end=' ')
    
    
def delete(arr, n, pos):
    # Shift elements to left
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]
    
    arr[n - 1] = 0  # clear last element
    return n - 1


n = delete(arr, n, 2)  # Delete element at index 2

print("\nAfter Delete:")
for i in range(n):
    print(arr[i], end=' ')
    
