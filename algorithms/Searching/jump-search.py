import math

def jumpsearch(arr, target, n):
    # jumpsearch is a searching alg works on Sorted Array.
    # Basic Idea: Check fewer elements than Binary Search by
    # Jumping some elements in place of searching all elements.
    step = math.sqrt(n)

    # finding block where it is present.
    prev = 0
    while arr[int(min(step, n)-1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            # if skipping steps is > total length of array.
            return -1

    # Now perform 'linear_search' for 'target' in block
    # beginning with 'prev' element.
    while arr[int(prev)] < target:
        prev += 1
        # if we reached next block or end of array,
        # then element is not present.
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == target:
        return prev

    return -1

# Driver code
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610]

target = 55
n = len(arr)

# Find the index of 'target' element.
indx = jumpsearch(arr, target, n)
print("Number {} is at index {}".format(target, indx))
