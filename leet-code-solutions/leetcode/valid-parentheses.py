class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={"(":")","{":"}","[":"]"}
        stack=[]
        for char in s:
            if char in hash_map:
                stack.append(hash_map[char])
            else:
                if len(stack)==0 or stack.pop()!=char:
                    return False
        return True if len(stack)==0 else False
        