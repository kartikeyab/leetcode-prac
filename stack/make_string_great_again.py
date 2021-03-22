class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            top_element = stack[-1] if stack else '$'
            if self.check_if_bad(top_element, char):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

    def check_if_bad(self, a, b):
        if a.isupper() and b.islower():
            if a.lower() == b:
                return True
            else:
                return False
        elif b.isupper() and a.islower():
            if b.lower() == a:
                return True
            else:
                return False

        
s = Solution()

print(s.makeGood("abBAcC"))