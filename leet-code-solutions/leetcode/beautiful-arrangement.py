class Solution:
    def countArrangement(self, n: int) -> int:
        counter=0
        def helperFunction(path,n,index):
            nonlocal counter
            if len(path[:])==n:
                counter+=1
                return 
            for num in range(1,n+1):
                if not (num%index==0 or index%num==0):
                    continue
                if num not in path:   
                    path.append(num)
                    helperFunction(path,n,index+1)
                    path.pop()
        helperFunction([],n,1)
        return counter


        