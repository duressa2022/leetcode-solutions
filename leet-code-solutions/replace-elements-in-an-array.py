class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        map={}
        for i,value in enumerate(nums):
            map[value]=i
        for u,v in operations:
            if u in map:
                nums[map[u]]=v
                map[v]=map[u]
        return nums
        