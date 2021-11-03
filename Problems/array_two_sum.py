"""
Given an array of integers and a 'target' integer,
find out the Indices which add up to the 'target' integer

Ex-1: 

Input: nums = [2, 7, 8, 11, 15], target = 9
Output: [0, 1]
Output: Because, nums[0] + nums[1] == 9, we return [0, 1]

Ex-2:

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Output: Because, nums[1] + nums[2] == 6, we return [1, 2]

Ex-3:

Input: nums = [3, 3], target = 6
Ouput: [0, 1]
Output: Because, nums[0] + nums[1] == 6, we return [0, 1]
"""
import array
from typing import List


class TwoSum:
    def two_sum(self, arr: List[int], target: int) -> List[int]:
        """
        1. Take the List of elements, a Target.
        2. Find the difference between Target and current element.
        3. This difference number is the remaining number we need to sum for the resultant target.
        4. We search for this resultant number in our Hashmap which keeps track of previous elements in our iteration
        instead of iterating again.
        """
        tracker = dict()

        for indx, element in enumerate(arr):
            # find difference
            diff = target - element

            # Check if this difference exist in our 'tracker'
            if diff in tracker:
                # then try to get that index and current index in the iteration
                # and return them.
                return [tracker[diff], indx]
            else:
                # keep track of this element as it might be
                # useful for our future iteration
                tracker[element] = indx

        return []


if __name__ == "__main__":
    # driver code
    elements = list(
        map(int, input("Enter the elements of an array: ").split(" "))
    )
    arr = array.array('i', elements)
    target = int(input("What's your target sum? "))

    # create TwoSum object and call the two_sum.
    # pass the 2 arguments. Input array & the Target
    two_sum_object = TwoSum()
    print(two_sum_object.two_sum(arr, target))
