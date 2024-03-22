class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[]
        i=0
        while i<length:
            if nums[i]<0:
                i=i+1
                continue
            correct=nums[i]-1
            if correct==i:
                i=i+1
            else:
                if nums[correct]==nums[i]:
                    result.append(nums[i])
                    nums[i]=-1
                else:
                    (nums[correct],nums[i])=(nums[i],nums[correct])
        return result



        