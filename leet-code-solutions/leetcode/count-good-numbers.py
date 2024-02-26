class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5
        primeCounter=(n)//2
        evenCounter=(n+1)//2
        return (self.power(5,evenCounter)*self.power(4,primeCounter))%(10**9 + 7)
    def power(self,x,n):
        if n==0:
            return 1
        else:
            temp=self.power(x,n//2)
            if n%2==0:
                return (temp**2)%(10**9 + 7)
            else:
                return (temp**2*x)%(10**9 + 7)



        