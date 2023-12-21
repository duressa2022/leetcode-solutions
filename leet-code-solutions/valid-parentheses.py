class Solution:
    def isValid(self, s: str) -> bool:
        map={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in map:
                stack.append(map[i])
            else:
                if len(stack)==0 or stack.pop()!=i:
                    return False
        return True if len(stack)==0 else False

        