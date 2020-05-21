'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    
    if n == 0:
        return 0
    
    return eating_cookies(n+1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

#base cases
# if n >=3, eat all
# subtract eated cookies from n, and recurse
# if n > 1, eat 2
# subtract eated cookies from n, and recurse
# if n > 0, eat 1
# subtract eated cookies from n, and recurse
# counter for every time n = 0