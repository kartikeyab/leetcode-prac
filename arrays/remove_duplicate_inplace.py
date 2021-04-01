"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]

Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.
"""

class Solution:
    def removeDuplicates(self, nums):
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
                i -= 1
            i += 1
        return nums
        

s = Solution()
print(s.removeDuplicates([0,0,0,0,0,1,1,1,2,2,3,3,3,4,4]))