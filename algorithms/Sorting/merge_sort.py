"""
Tutorial followed: DSA - Treehouse - Freecodecamp on YouTube.
Source Link: https://www.youtube.com/watch?v=8hly31xKli0&t=751s
"""


def merge_sort(nums_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide them into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous steps

    Takes: O(n log n)
    So actually in Python: O(kn log n)
    """

    # if given empty list or list with only 1 element, we return the list as is.
    if len(nums_list) <= 1:
        return nums_list

    # Divide lists to sublists
    left_half, right_half = split(nums_list)
    print("Left half: ", left_half)
    print("Right half: ", right_half)

    # Conquer sublists
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Combining
    return merge(left, right)


def split(nums_list):
    """
    Divide the unsorted list at MID POINT into sublists.
    Returns 2 Sublists. Left, Right.

    Takes: O(log n) time
    So actually in Python: O(k log n) time due to Slicing which takes O(k) time. where K = size of Slice.
    """
    mid_point = len(nums_list) // 2  # round-down
    # use slicing notation to extract the portion we want to return
    # SLICING in python takes O(K) time where K = elements in the Slice.
    left = nums_list[:mid_point]
    right = nums_list[mid_point:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns the new merged list.

    Takes: O(n) time. 'n' number of Merge steps.
    """
    l = []
    i = 0   # index for the left list
    j = 0   # index for the right list
    print("Passed left half and right half are: {}, {}".format(left, right))

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # If RIGHT list is shorter than the LEFT.
    # If Right list reached the end than the Left list.
    print("i value: {} and j value: {}".format(i, j))
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    print("After sorted: {}".format(l))
    return l


def verify_sorted(nums_list):
    n = len(nums_list)

    if n == 0 or n == 1:
        return True

    return nums_list[0] < nums_list[1] and verify_sorted(nums_list[1:])


alist = [78, 22, 43, 19, 15, 9, 81, 56, 42]
l = merge_sort(alist)
print(verify_sorted(l))
