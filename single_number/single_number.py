'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    
    # # 1
    # return 2 * sum(set(arr)) - sum(arr) 
    
    # 2 
    # for v in arr:
    #     if arr.count(v) == 1:
    #         return v

    ## 3
    ## O(n^2)
    # no_dupes = []
    # for v in arr:
    #     if v not in no_dupes:
    #         no_dupes.append(v)
    #     else:
    #         no_dupes.remove(v)
    
    # return no_dupes[0]

    # 4
    # O(2 * n) ~ O(n)
    # counts = {}

    # for v in arr:
    #     if v in counts:
    #         counts[v] += 1
    #     else:
    #         counts[v] = 1
    
    # for num in counts:
    #     if counts[num] == 1:
    #         return num





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/


# set = will filter out duplicates, only have unique values
# multiplying this by 2 will double the value, as if there were duplicates
# subtract the total of the original array
# the difference will be unique number in arr