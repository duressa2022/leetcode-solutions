class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def helperFunction(current,temp):
            if len(current)==len(temp):
                result.append(temp[:])
            
            for num in current:
                if num not in temp:
                    temp.append(num)
                    helperFunction(current,temp)
                    temp.pop()
        helperFunction(nums,[])
        return result

        