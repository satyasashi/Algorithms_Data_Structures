"""
Faster than Binary search.
Key is, We JUMP by few STEPS in array till we find the element at JUMPED position
is LESS than TARGET value we are looking for by keeping Trace of PREVIOUSLY JUMPED
Position.

Once that's done, we run a Linear Search from PREVIOUS INDEX till we find TARGET
element.
"""
import math
def jumpSearch(arr, target, size):
    steps_to_jump = math.sqrt(size)
    pointer_to_prev_step_jumped = 0
    while arr[int(min(steps_to_jump, size))] < target:
         pointer_to_prev_step_jumped = steps_to_jump
         steps_to_jump += math.sqrt(size)

    while arr[int(min(pointer_to_prev_step_jumped, size))] < target:
        pointer_to_prev_step_jumped += 1

    if arr[int(pointer_to_prev_step_jumped)] == target:
        return int(pointer_to_prev_step_jumped)
    return False

arr = [1, 3, 4, 5, 6, 10, 20, 40, 43, 90]
target = 3
size = len(arr)-1
res=jumpSearch(arr, target, size)
print(res)
