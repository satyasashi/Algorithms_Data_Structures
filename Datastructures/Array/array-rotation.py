''' 
Rotation of the array elements means, taking few elements in the Array
and Moving them to other side of the array. Rotations can be Left rotation 
or Right rotation.
 '''

# arr = Holds the array elements
# num_of_ele = Holds number of elements to be rotated.
# size = Holds the Total Number of elements in the Array.

def leftRotate(arr, num_of_ele, size):
    # for i < num_of_elements, do this.
    for i in range(num_of_ele):
        leftRotatebyOne(arr, size)


def leftRotatebyOne(arr, size):
    '''left rotation is done by taking arr[0] element to temporary variable,
    and moving all the adjacent elements to front. 
    i.e., arr[1] --> arr[0], arr[2] --> arr[1] and so on

    Now all the elements are moved to Left by ONE step which makes the End
    of the Array index EMPTY. Now fill that Empty Space with our TEMP variable
    which is holding the Element we want to rotate.'''

    temp = arr[0] # Took an element.

    for i in range(size-1):
        # Move all the remaining elements one step left.
        arr[i]=arr[i+1]

    # Now assign the element we took to last empty index.
    arr[size-1] = temp

def printArray(arr, size):
    for i in range(size):
        print("{}".format(arr[i]), end=" ")


if __name__=="__main__":
    arr = [3, 6, 2, 8, 2, 9, 12]
    num_of_ele = 2
    size = len(arr)
    
    leftRotate(arr, num_of_ele, size)

    # print the values in the array
    printArray(arr, size)
