class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter=Counter(nums)
        length=len(nums)
        result=set()
        def helperFunction(path):
            if len(path)==length:
                result.add(tuple(path[:]))
                return 
            for num in nums:
                if counter[num]!=0:
                    counter[num]-=1
                    path.append(num)
                    helperFunction(path)
                    counter[num]+=1
                    path.pop()
        helperFunction([])
        final=[]
        for value in result:
            final.append(list(value))
        return final
        