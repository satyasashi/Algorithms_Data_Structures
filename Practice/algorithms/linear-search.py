def linear_search(arr, target, size):
    for i in range(size):
        if arr[i] == target:
            return True
    return False

"""
Case 1: Element present in Array.
Loop through and check if the present item is
our target. If Yes, return True.

Case 2: If element is not present, return False
"""

arr = [8,2,1,3,5,4,8,0,18,20]
target = 15

res = linear_search(arr, target, len(arr))
print(res)
