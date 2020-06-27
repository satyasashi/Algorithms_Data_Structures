def fibonnaci_search(arr, target, size):
    # fibonnaci numbs 0 1 1 2 3 5 8 13 21 34
    fibM2 = 0
    fibM1 = 1
    fibM = fibM2 + fibM1

    while(fibM <= size):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1

    offset = -1

    while (fibM >= 1):
        # make the Index
        i = min(offset+fibM2, size-1)

        if arr[i] < target:
            # we move 1 down.
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        elif arr[i] > target:
            # we move 2 down.
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        else:
            return i

    # if(fibM1 and arr[offset+1] == target):
    #     print("Found element")
    #     return offset+1

    return -1


arr = [20, 30, 43, 45, 59, 50, 55, 56, 59, 61, 66, 68, 70]
target = 70
size = len(arr)
res = fibonnaci_search(arr, target, size)
print(res)
