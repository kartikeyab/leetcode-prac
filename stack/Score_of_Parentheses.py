"""
856. Score of Parentheses
Medium

Given a balanced parentheses string s, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
Example 4:

Input: s = "(()(()))"
Output: 6

"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        z = [0]
        for i in S:
            if i == '(':
                z.append(0)
            else:
                x = z.pop()
                z[-1] += max(2*x,1)
        print(z)
        return z[0]

s = Solution()
print(s.scoreOfParentheses("((()))"))
