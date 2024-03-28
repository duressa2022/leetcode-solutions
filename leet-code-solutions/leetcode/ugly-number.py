class Solution:
    def isUgly(self, n: int) -> bool:
        def solver(n):
            result=set()
            d=2
            while d*d<=n:
                while n%d==0:
                    result.add(d)
                    n=n//d
                d=d+1
            if n>1:
                result.add(n)
            return result
        factors=solver(n)
        if n<=0:return False
        if n<2:return True
        holder={2,3,5}
        for num in factors:
            if num  not in holder:
                return False
        return True



        