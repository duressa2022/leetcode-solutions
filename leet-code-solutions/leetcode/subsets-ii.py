class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def helperFunction(nums,path,right):
            if sorted(path) not in result:
                result.append(sorted(path[:]))
            for i in range(right,len(nums)):
                path.append(nums[i])
                helperFunction(nums,path,i+1)
                path.pop()
        helperFunction(nums,[],0)
        return result
        