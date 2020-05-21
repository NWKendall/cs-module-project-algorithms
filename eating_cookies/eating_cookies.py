'''
Input: an integer
Returns: an integer
'''

def eating_cookies(cookies, ways=None):
    # Your code here
    # base cases
    if ways is None:
        ways = {}
    if cookies < 2:
        return 1
    elif cookies == 2:
        return 2
    elif cookies == 3:
        return 4
    elif ways and ways[cookies]:
        return ways[cookies]
    else:
        ways[cookies] = eating_cookies(cookies-1, ways) + eating_cookies(cookies-2, ways) + eating_cookies(cookies-3, ways)
    
    return ways[cookies]


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