''' 
Rotation of the array elements means, taking few elements in the Array
and Moving them to other side of the array. Rotations can be Left rotation 
or Right rotation.
'''

'''
This is an extension of method 2 [Array-Rotation]. But Instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets.
If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved 
within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally 
store temp at the right place.
'''

# def leftRotate(arr, num_of_ele, total_size_arr):
#     for i in range(gcd(d, n)):

#         temp = arr[i]
#         index_track = i
#         while 1:
#             k = index_track+num_of_ele
#             if k > total_size_arr:
#                 k = k - total_size_arr
#             if k == i:
#                 break

#             arr[j] = 


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# Driver program to test above functions
arr = [1,2,3,4,5,6,7,8]

# leftRotate(array, num_of_ele, total_size_arr)
# leftRotate(arr, 2, 7)

# Print the effected array
# printArray(arr)

gcd_value = gcd(5, 12)
print(gcd_value)