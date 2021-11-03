from Datastructures.linked_list.linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linkedlist in ascending order.
    - First recursively divide the linkedlist to sublists containing a single node.
    - Repeatedly merge the sublists to produce sorted sublists until one remains.

    Return the sorted linkedlist
    """
    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    pass
