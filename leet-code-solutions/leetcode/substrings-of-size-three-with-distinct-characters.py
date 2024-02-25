class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result=0
        left=0
        right=2
        while right<len(s):
            if self.isUnique(s[left:right+1]):
                result+=1
            left=left+1
            right=right+1
        return result
    def isUnique(self,string):
        return len(set(list(string)))==3


        