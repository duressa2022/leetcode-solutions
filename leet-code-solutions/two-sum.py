class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in map:
                return [i,map[find]]
            map[nums[i]]=i
        return []
        