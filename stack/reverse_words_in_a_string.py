class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        for char in s:
            top_element = stack[-1] if stack else '$'
            if top_element == char == ' ':
                continue
            else:
                stack.append(char)
        normal = "".join(stack)
        rev = normal.split(' ')[::-1]
        final = []
        for i in rev:
            if i:
                final.append(i)
        return " ".join(final)

    

s = Solution()
print(s.reverseWords("     HI HOW   ARE you   "))