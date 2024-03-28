class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def solver(n):
            primes=[True for i in range(n+1)]
            primes[0]=primes[1]=False
            d=2
            while d*d<=n:
                if primes[d]:
                    i=d*d
                    while i<=n:
                        primes[i]=False
                        i=i+d
                d=d+1
            return [index for index in range(n+1) if primes[index]==True]
        if n<2:return []
        primes=solver(n)
        left,right=0,len(primes)-1
        result=[]
        while left<=right:
            if primes[left]+primes[right]==n:
                result.append([primes[left],primes[right]])
            if primes[left]+primes[right]>n:
                right=right-1
            else:
                left=left+1
        return result



        