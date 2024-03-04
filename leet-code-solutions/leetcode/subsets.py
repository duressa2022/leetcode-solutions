class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def helperFunction(nums,right,path):
            result.append(path[:])

            for i in range(right,len(nums)):
                path.append(nums[i])
                helperFunction(nums,i+1,path)
                path.pop()

        helperFunction(nums,0,[])
        return list(result)
        