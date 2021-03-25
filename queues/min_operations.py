"""
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
"""

class Solution:
    def minOperations(self, logs):        
        count = 0
        
        for char in logs:

            if char == "../":
                if count == 0:
                    count = count
                else:
                    count -= 1                    
            elif char  == "./":
                count += 0                    
            else:
                count += 1
        return count

s = Solution()
print(s.minOperations(["./","../","../","../"]))