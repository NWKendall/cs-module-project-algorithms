'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, cache=None):
    # Your code here
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

#base cases
# if n >=3, eat all
# subtract eated cookies from n, and recurse
# if n > 1, eat 2
# subtract eated cookies from n, and recurse
# if n > 0, eat 1
# subtract eated cookies from n, and recurse
# counter for every time n = 0

# append each eating method into ways
# check sub arrays are unique (no duplicates)
# return len of arrays


# ways[0] = [1,1,1,1,1] == 5
# ways[1] = [2,1,1,1] == 5
# ways = [[1,1,1,1,1], [2,1,1,1]...etc]
# check for uniqueness of subarays (no dupes)
# return len(ways)