class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixCounter=defaultdict(int)
        prefixCounter[0]=1
        runningSum=0
        counter=0
        for num in nums:
            runningSum+=num
            if runningSum%k in prefixCounter:
                counter+=prefixCounter[runningSum%k]
            prefixCounter[runningSum%k]+=1
        return counter
        