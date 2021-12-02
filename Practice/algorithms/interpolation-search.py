"""
Faster than JUMP search and Binary Search.
Instead of finding steps by using probing formula.
"""
def interpolationSearch(arr, target, size):
    low = 0
    high = size
    while low <= high and target >= arr[low] and target <= arr[high]:
        print("LOW: ",low)
        if low == high:
            if arr[low] == target:
                return low
            # When element doesn't exist
            print("Element doesn't exist")
            return False

        # Probing formula to find the position
        pos = low + int((float(high-low)/(arr[high]-arr[low])) * (target-arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        elif arr[pos] > target:
            high = pos - 1
    return False

arr = [1, 3, 4, 5, 6, 10, 20, 40, 43, 90]
target = 2
res = interpolationSearch(arr, target, len(arr)-1)
print(res)
