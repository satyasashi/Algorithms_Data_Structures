"""
Fibonnaci Search:
Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.

Differences with Binary Search:

    Fibonacci Search divides given array in unequal parts
    Binary Search uses division operator to divide range. Fibonacci Search doesn’t use /, but uses + and -. The division operator may be costly on some CPUs.
    Fibonacci Search examines relatively closer elements in subsequent steps. So when input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.

F(n) = F(n-1) + F(n-2) + F(n-3) ... + F(n-m)
F(0) = 0
F(1) = 1

ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
https://www.geeksforgeeks.org/fibonacci-search/
"""


def fibonnaci_search(arr, target, size):
    # initiate the Fibonacci numbers
    fibM2 = 0  # (m-2)'th Fibonnaci number
    fibM1 = 1  # (m-1)'th Fibonacci number
    fibM = fibM2 + fibM1  # m'th Fibonacci
    print("Initially FibM2, FibM1, FibM : {}, {}, {}".format(fibM2, fibM1, fibM))
    while(fibM < size):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1
        print("FibM2, FibM1, FibM : {}, {}, {}".format(fibM2, fibM1, fibM))

    # Eliminated range from Front
    offset = -1

    while(fibM > 1):
        print("iter: ")
        # check if fibM2 is Valid index
        i = min(offset+fibM2, size-1)
        print("i value: {}".format(i))
        # if Target > value at Index 'i' (FibM2), cut
        # the subarray array from offset to i
        if arr[i] < target:
            # move one down
            print("arr[{}]--> {} < {}".format(i, arr[i], target))
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
            print("******************************")
            print("FibM2, FibM1, FibM : {}, {}, {}".format(fibM2, fibM1, fibM))
        elif arr[i] > target:
            # move two down
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
            print("-------------------------------")
            print("FibM2, FibM1, FibM : {}, {}, {}".format(fibM2, fibM1, fibM))
        else:
            print("Found element:")
            return i


    if(fibM1 and arr[offset+1] == target):
        print("Found element")
        return offset+1

    return -1


arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
target = 90
size = len(arr)

res = fibonnaci_search(arr, target, size)
print(res)
