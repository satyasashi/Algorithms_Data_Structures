# BINARY SEARCH O(Logn)
# Take list of sorted items, divide the list by half and take the element
# Compare with 'target' element, If picked number is less than 'Target',
# then ignore all elements towards left. Now starting element will be next
# element from element compared just now.

def binary_search_rec(arr, target):
    for i in range(0, len(arr)-1):
        half = len(arr)//2
        print(half, i)
        if arr[half] == target:
            print("Found element {} at index {}".format(arr[half], half))
            return half
        elif arr[half] < target:
            print("half < target")
            arr = arr[half+1:]
            print(arr)
            return binary_search(arr, target)
        elif arr[half] > target:
            print("half > target")
            arr = arr[0:half-1]
            return binary_search(arr, target)
    return -1


def binary_search_iter(arr, l, r, target):
    while l <= r:
        mid = (l+r)//2 # find mid value
        print(mid, end="\n")

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            l = mid+1

        else:
            r = mid-1

    return False


arr = [0, 0, 0, 12, 14, 17, 25]
target = 10

res = binary_search_iter(arr, 0, len(arr)-1, target)
# res = binary_search_rec(arr, target)
print(res)
