"""
Input: nums = [0,1,0,3,12]
[0,1,0,3,12]
[1,0,]
[1,0,0,3,12]
[1,0,3,12,0]
[1,3,0,12,0]
[1,3,12,0,0]

Output: [1,3,12,0,0]
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count += 1

        while 0 in nums[:len(nums)-count]:     
            i = 0
            j = 1
            while i < len(nums)-1:
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                
                i += 1
                j += 1
        return nums

s = Solution()
print(s.moveZeroes([1,2,3,0,0,0,3,4,0,5,0,0,3,0,2,1,0]))
            

