class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter=Counter(s)
        number=counter["1"]
        s=sorted(s,reverse=True)
        left,right=0,1
        while right<len(s):
            if s[left]=="1" and s[right]=="0":
                (s[left],s[right])=(s[right],s[left])
            left=left+1
            right=right+1
        return "".join(s)