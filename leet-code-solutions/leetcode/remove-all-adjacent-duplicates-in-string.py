class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=["-1"]
        for char in s:
            if stack[-1]!=char:
                stack.append(char)
            else:
                while stack[-1]==char:
                    stack.pop()
        return "".join(stack[1:])
        