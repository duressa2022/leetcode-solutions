class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counter=defaultdict(int)
        left=result=0
        length=len(nums)
        for right in range(length):
            counter[nums[right]]+=1
            while right-left+1-counter[1]>k:
                counter[nums[left]]-=1
                left=left+1
            result=max(result,right-left+1)
        return result
        
        