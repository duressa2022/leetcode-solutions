class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        result=0
        while x>0:
            result*=10
            result+=x%10
            x=x//10
        if result<-2**31 or result>2**31-1:
            return 0
        return sign*result

        
        