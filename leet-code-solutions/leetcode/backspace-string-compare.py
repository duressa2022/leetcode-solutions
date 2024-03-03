class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackString1=[]
        stackString2=[]
        for char in s:
            if char!="#":
                stackString1.append(char)
            else:
                if stackString1:
                    stackString1.pop()
        for char in t:
            if char!="#":
                stackString2.append(char)
            else:
                if stackString2:
                    stackString2.pop()
        sString="".join(stackString1)
        tString="".join(stackString2)
        return sString==tString


        