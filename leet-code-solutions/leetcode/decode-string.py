class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!="]":
                stack.append(char)
            else:
                temp=""
                while stack and stack[-1]!="[":
                    temp=stack.pop()+temp
                stack.pop()
                tempNumber=""
                while stack and stack[-1].isdigit():
                    tempNumber=stack.pop()+tempNumber
                temp*=int(tempNumber)
                stack.append(temp)
        return "".join(stack)

  

        