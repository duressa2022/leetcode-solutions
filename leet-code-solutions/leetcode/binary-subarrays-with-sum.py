class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixCounter=defaultdict(int)
        prefixCounter[0]=1
        runningSum=0
        counter=0
        for num in nums:
            runningSum+=num
            if runningSum-goal in prefixCounter:
                counter+=prefixCounter[runningSum-goal]
            prefixCounter[runningSum]+=1
        return counter