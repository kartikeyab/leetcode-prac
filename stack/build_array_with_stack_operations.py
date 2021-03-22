class Solution:
    def buildArray(self, target,n):
        arr = []
        for i in range(1,n+1):
            if i in target:
                arr.append("Push")
            else:
                arr.append("Push")
                arr.append("Pop")
            if i == target[-1]:
                return arr
 
        return arr
        
s = Solution()

print(s.buildArray(target = [1,2,3,6], n=6))