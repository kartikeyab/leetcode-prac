"""
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

"""

class Solution:
    def calPoints(self, ops):
        stack = []
        
        for char in ops:
            top_element = stack[-1] if stack else '#'
            if char == "C":
                stack.pop()
            elif char == "D":
                stack.append(2*top_element)
            elif char == "+":
                stack.append(stack[-1]+stack[-2]) 
            else:
                char = int(char)
                stack.append(char)

        return sum(stack)

s = Solution()
print(s.calPoints([]))