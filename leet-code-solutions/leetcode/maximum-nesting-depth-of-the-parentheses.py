class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        length=-float("inf")
        current=0
        for char in s:
            if char=="(":
                if stack:
                    current+=len(stack)
                stack.append(char)
                length=max(current,length)
                current=0
            else:
                if char==")":
                    stack.pop()
                    current+=1
        return max(length,current)

        