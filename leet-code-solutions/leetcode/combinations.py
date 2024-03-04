class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        def helperFunction(number,result):
            if len(result)==k:
                answer.append(result[:])
                return
            for num in range(number,n+1):
                result.append(num)
                helperFunction(num+1,result)
                result.pop()
        result=[]
        helperFunction(1,[])
        return answer
        