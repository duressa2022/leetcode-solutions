class Solution:
    def myPow(self, x, n) -> float:
        if n<0:
            n=-n
            x=1/x
        if n==0:return 1
        else:
            result=self.myPow(x,n//2)
            result=result**2
            if n%2==1:
                result*=x
            return result




        