"""
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.
"""


def interpolation_search(arr, target, n):
    low = 0
    high = n-1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Formula to find position with keeping uniform
        # distribution in mind.

        #   low +        high - low
        #          ------------------   x (target - arr[low])
        #           arr[high] - arr[low]
        pos = low + int((  (float(high-low)/(arr[high]-arr[low])) * (target - arr[low])  ))

        print(pos)
        if arr[pos] == target:
            return pos

        elif arr[pos] < target:
            low = pos + 1
        elif arr[pos] > target:
            high = pos - 1

    return -1
    print("Invalid target")


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35]
interpolation_search(arr, 24, len(arr))
