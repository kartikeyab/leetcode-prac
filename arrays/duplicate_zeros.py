"""
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

class Solution:
    def duplicateZeros(self, arr):
        orig_l = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr = arr[:i+1] + [0] + arr[i+1:]
                i += 1
            i += 1
        arr = arr[:orig_l]
        print(arr)


s = Solution()
print(s.duplicateZeros([1,0,0,2,3,0,4,5,0,4]))

        
