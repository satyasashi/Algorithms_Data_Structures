def binary_rec_search(arr, l, r, target):
    print("passed args: {}, {}".format(l, r))
    if l <= r:
        mid = l + (r-l)//2
        print("MID: ", mid)
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binary_rec_search(arr, mid+1, r, target)
        elif arr[mid] > target:
            return binary_rec_search(arr, l, mid-1, target)
    return False

def binary_search_iterative(arr, l, r, target):
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return False

"""
Case 1: MID element is Target, return True
Case 2: If MID smaller than Target, binary_search from
next element of present MID till N-1 array.
Case 3: If MID greater than Target, binary_search from
Beginning to previous element of MID.
Note: To keep track of Indices, use L & R to hold them.
L --> Holds left part of array,
R --> Holds Right part of Array.
"""
arr = [1, 3, 4, 5, 6, 10, 20, 40, 43, 90]
target = 40

res = binary_search_iterative(arr, 0, len(arr)-1, target)
print(res)
