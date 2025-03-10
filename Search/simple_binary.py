def binary_search(arr, target, left, right):
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, right)

        else:
            return binary_search(arr, target, left, mid - 1)  # Corrected here

    else:
        return -1

input_array = input("Enter array as comma-separated: ")
target = int(input("Enter target value: "))

arr = list(map(int, input_array.replace(",", " ").split()))

arr.sort()
print(arr)
result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
