class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        hashMap={"(":")","{":"}","[":"]"}
        validCounter=0
        stack=[]
        for char in s:
            if char in hashMap:
                stack.append(hashMap[char])
            else:
                if len(stack)>0 and stack.pop()==char:
                    validCounter+=1
        return len(s)-validCounter*2
        