"""
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""

class Solution:
    def backspaceCompare(self, S, T):
        stack1 = []
        stack2 = []
        for char in S:      
            if char == "#":
                if stack1:
                    stack1.pop()
                else:
                    continue       
            else:
                stack1.append(char)        
        for char in T:
            
            if char == "#":
                if stack2:
                    stack2.pop()
                else:
                    continue    
            else:
                stack2.append(char)

        print(stack1)
        print(stack2)
        return stack1==stack2
                
s = Solution()      
print(s.backspaceCompare(S = "ab##", T = "c#d#"))