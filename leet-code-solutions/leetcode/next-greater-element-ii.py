class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result=[-1]*len(nums)
        stack=[]
        for i in range(2):
            for j,num in enumerate(nums):
                while stack and nums[stack[-1]]<num:
                    result[stack[-1]]=num
                    stack.pop()
                stack.append(j)

        return  result

        