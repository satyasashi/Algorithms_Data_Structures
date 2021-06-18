
# Given 'n' elements in array, searching for an element in it, takes
# O(n) time, as it needs to loop each and every element and compare it with
# our target element.

def linear_search(arr, n, target):
    for i in range(n):
        print("Operation ", i)
        if arr[i] == target:
            return i

    return -1


arr = [4,6,2,3,9,12,23,0,9,22]
n = len(arr)
target = 99 # Does 'n' iterations to find element.

res = linear_search(arr, n, target)
print(res)
