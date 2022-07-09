def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Insertion sorted array is ", arr)

def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    print("Selection sorted array is ", arr)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def linear_search(arr, y):
    for i in range(len(arr)):
        if arr[i] == y:
            return i
    return -1

# Driver Input
arr = []
n = int(input("Enter number of array elements : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print("The Unsorted array is: ", arr)

# Sort the arrays
insertion_sort(arr)
selection_sort(arr)

# For Binary Search
x = int(input("Enter the value of x for Binary search in the given array: "))
binary_result = binary_search(arr, x)
if binary_result != -1:
    print("The Element is present at index", str(binary_result))
else:
    print("The Element is not present in array")

# For Linear Search
y = int(input("Enter the value of y for Linear search in the given array: "))
linear_result = linear_search(arr, y)
if linear_result != -1:
    print("The Element is present at index", str(linear_result))
else:
    print("The Element is not present in array")
