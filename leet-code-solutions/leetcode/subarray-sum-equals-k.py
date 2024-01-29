class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCounter=defaultdict(int)
        prefixCounter[0]=1
        runningsum=0
        counter=0
        for num in nums:
            runningsum+=num
            if runningsum-k in prefixCounter:
                counter+=prefixCounter[runningsum-k]
            prefixCounter[runningsum]+=1
        return counter
            



        