"""
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        diff = {}
        
        for pos, val in enumerate(nums2):
            
            while stack and stack[-1] < val:
                diff[stack.pop()] = val
            
            stack.append(val)
            print(stack)
            print(diff)
        for pos in range(len(nums1)):
            
            if nums1[pos] in diff:
                nums1[pos] = diff[nums1[pos]]
            else:
                nums1[pos] = -1
        
        return nums1

s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))