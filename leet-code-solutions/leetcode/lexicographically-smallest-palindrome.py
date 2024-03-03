class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        result=["0"]*len(s)
        left,right=0,len(s)-1
        while left<=right:
            if s[left]>s[right]:
                result[left]=s[right]
                result[right]=s[right]
            else:
                result[left]=s[left]
                result[right]=s[left]
            left=left+1
            right=right-1

        return "".join(result)


        