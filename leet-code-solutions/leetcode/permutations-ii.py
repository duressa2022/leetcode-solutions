class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter=Counter(nums)
        tempResult=set()
        finalResult=[]
        length=len(nums)
        def helperFunction(path):
            if length==len(path):
                tempResult.add(tuple(path[:]))
                return 
            for num in nums:
                if counter[num]!=0:
                    path.append(num)
                    counter[num]-=1
                    helperFunction(path)
                    counter[num]+=1
                    path.pop()
        helperFunction([])
        for result in tempResult:
            finalResult.append(list(result))
        return finalResult
