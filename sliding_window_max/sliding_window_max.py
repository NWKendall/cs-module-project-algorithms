'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # length of k
    diameter = [None] * k
    max_arr = []
    radius = len(nums) - k + 1
    for i in range(radius):
        for j in range(len(diameter)): # 3
            diameter[j] = nums[i + j]
            print(diameter[j])
        print("#####")
        max_arr.append(max(diameter))
    # push max value of array

    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3  
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# Expected Output: [3,3,5,5,6,7] 

#####
# U #
#####

# an array with length = k, slides over values in array, and for each instance, returns the highest value that k encapsulates

# analaogy
# a microscope has the diameter of k 
# We select/return the largest specimen we can see within the range of k
# after, the microscope shifts through the list of specimens one at a time until k touches the end of the list

# not a matrix, more a single array that has multiple computations
# return an array of max value from each iteration
    # (len(arr) - len(k)) + 1 values in answer? ✅


# Window position                Max
# ---------------               -----
# [1  3  -1  -3  5] 3  6  7       5
#  1 [3  -1  -3  5  3] 6  7       5
#  1  3 [-1  -3  5  3  6] 7       6
#  1  3  -1 [-3  5  3  6  7]      7

# 8 - 5 = 3
# 3 + 1 = 4

#####
# P #
#####

# receive array and k
# k = [None] * len(k)
# compare values in k and push highest to max