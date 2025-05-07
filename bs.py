def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found at index mi
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(numbers, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")
