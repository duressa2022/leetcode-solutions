class Solution:
    def numberOfMatches(self, n: int) -> int:
        result=0
        while n>1:
            if n%2==0:
                result+=n/2
                n=n/2
            else:
                result+=(n-1)/2
                n=(n-1)/2+1
        return int(result)
        