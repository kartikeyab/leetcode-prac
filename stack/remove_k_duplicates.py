
def removeDuplicates(s: str, k: int) -> str:
    stack = ""
    for char in s:
        if len(stack) > 0 and stack[-k+1:]  == char*(k-1):
            stack = stack[:-k+1] 
        else:
            stack += char
    return stack


print(removeDuplicates(s = "aaaabcddddd", k = 4))
