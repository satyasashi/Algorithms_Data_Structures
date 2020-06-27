# In EXPONENTIAL SEARCH, you find the RANGE where the Target element exist
# by increasing constantly by *2 (exponent).
# Then you perform BINARY SEARCH on that piece of Array.

def binary_search(arr, target, start, end):
    print( arr, target, start, end)
    while arr[start] <= target:
        mid = (start + end)//2
        print("MID :", mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
            return binary_search(arr, target, start, end)
        else:
            end = mid-1
            return binary_search(arr, target, start, end)

    return False


def exponential_search(arr, target, size):
    # 0 * 2 is always 0. So it's going to be exceptional.
    if arr[0] == target:
        return '0'

    if target < arr[0] or target > arr[size]:
        return False

    i = 1
    while i <= size and arr[i] < target:
        # luckily during this exponential increment, if we found target.
        if arr[i] == target:
            return i
            
        # exponentially increase the Index till it's less than our Array size
        i = i * 2
        print("incremented")

    start = i//2
    print("Start: ", start)
    end = size
    res = binary_search(arr, target, start, end)

    if res is False:
        print("Element not found.")

    return res


arr = [23, 25, 30, 45, 55, 67, 70, 82, 93, 100, 123, 151, 166]
size = len(arr)-1
target = 200

res = exponential_search(arr, target, size)
print(res)
