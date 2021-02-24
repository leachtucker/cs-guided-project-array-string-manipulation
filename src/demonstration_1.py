"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    # Can easily be solved without a dictionary. That would require less space and might be a more efficient solution
    # sum1 = left over our index i. sum2 = right of our index i
    pivots = {} # key, code --> _int_ index, _tuple_ (sum1, sum2)

    sum1 = 0
    for i in range(0, len(nums)):
        sum1 += nums[i]

        sum2 = 0
        for j in range(i, len(nums)):
            sum2 += nums[j]

        pivots[i] = (sum1, sum2)

    for key, value in pivots.items():
        if value[0] == value[1]:
            return key

    return -1

print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
