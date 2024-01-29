class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length=len(nums)
        prefixCounter=[0]*(length)
        for [start,end] in requests:
            prefixCounter[start]+=1
            if end+1<length:
                prefixCounter[end+1]-=1
        for index in range(1,length):
            prefixCounter[index]+=prefixCounter[index-1]
        prefixCounter.sort()
        nums.sort()
        result=0
        for index in range(length):
            result+=nums[index]*prefixCounter[index]
        return result%(10**9+7)



        