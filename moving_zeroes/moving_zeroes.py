'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] is not 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr=[0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
# ALWAYS SWAPS THE FIRST ZERO WITH THE LAST NON ZERO
# in place solution
# two pointers i and j
# i only increases if swapping with j AND when j is not a zero