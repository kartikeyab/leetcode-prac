"""
Input: [1,1,0,1,1,1]
[0,1,0,0,1,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.


[2,4,5,8]
[2,1,3]
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_c = 0
        c = 0
        
        for i in nums:
            if i == 1:
                c += 1
                max_c = max(max_c, c)
            else:
                c = 0

        return max_c


s = Solution()
print(s.findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
            