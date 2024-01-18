class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hash_map={}
        left=right=0
        current=0
        while right<len(nums):
            if nums[right] !=0:
                right=right+1
            else:
                if nums[right] not in hash_map:
                    hash_map[nums[right]]=right
                else:
                    current=max(current,right-left-1)
                    left=hash_map[nums[right]]+1
                    hash_map[nums[right]]=right
                right=right+1
        return max(current,right-left-1)
            

