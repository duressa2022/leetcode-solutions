class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!=")":
                stack.append(char)
            else:
                string=[]
                while stack and stack[-1]!="(":
                    string.append(stack.pop())
                stack.pop()
                for char in string:
                    stack.append(char)
        return "".join(stack)
        