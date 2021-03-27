"""
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums):
        c  = 0
        for i in nums:
            if self.check_dig(i) % 2 == 0:
                c += 1
        return c


    def check_dig(self,num):
        if num == 0:
            return 0
        return 1 + self.check_dig(num//10)



s = Solution()

print(s.findNumbers([12,345,2,6,7896]))
