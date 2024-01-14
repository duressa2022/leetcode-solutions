class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter=0
        left=0
        right=0
        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                left=left+1
                right=right+1
                counter+=1
            else:
                right=right+1
        return counter==len(s)

        