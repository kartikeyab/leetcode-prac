"""
1047. Remove All Adjacent Duplicates In String


Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for char in s:
            top_element = stack[-1] if stack else '$'
            if char == top_element:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

s = Solution()

print(s.removeDuplicateLetters('deeedbbcccbdaa'))