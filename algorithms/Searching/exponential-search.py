# Exponential search includes 2 Steps:
# 1. Find RANGE where element is present
# 2. Do a BINARY SEARCH on the given Range.

def binary_search(arr, l, r, target, n):
    # Take an array, find MID, check if it's TARGET, else again
    # Half it and go on until you find element, or return False
    while r >= l and n > 0 and l <= n and r <= n:
        mid = (l+r)//2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return False


def exponential_search(arr, target, n):
    # if 0th element is target return it.
    if arr[0] == target:
        return i

    # Out of Array check.
    if target < arr[0] or target > arr[n-1]:
        return "No values for your search in our array"
    # From 1st Index, lets check if it's TARGET and move the index
    # TWICE and check if it's TARGET until you find that Element at that Index
    # is LESS than your TARGET element.
    i = 1
    while n > 0 and i <= n and arr[i] <= target:
        if arr[i] == target:
            return i
        i = i * 2
        print(i)


    l = i//2
    r = min(i, n-1)
    return binary_search(arr, l, r, target, n)


arr = [23, 25, 30, 45, 55, 67, 70, 82, 93, 100, 123, 151, 166]
n = len(arr)
target = 25
print("Length of array: ", n)
res = exponential_search(arr, target, n)
print(res)
