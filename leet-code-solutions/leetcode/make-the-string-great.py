class Solution:
    def makeGood(self, s: str) -> str:
        stack=["-1"]
        for char in s:
            if char.islower() and stack[-1].isupper():
                if char.upper()==stack[-1].upper():
                    stack.pop()
                else:
                    stack.append(char)
            elif char.isupper() and stack[-1].islower():
                if char.upper()==stack[-1].upper():
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack[1:])

        