# BINARY SEARCH O(Logn)
# Take list of sorted items, divide the list by half and take the element
# Compare with 'target' element, If picked number is less than 'Target',
# then ignore all elements towards left. Now starting element will be next
# element from element compared just now.

def binary_search(arr, target):
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

arr = [7,8,9,12,89,98,104,893]
target = 9

res = binary_search(arr, target)
print(res)
