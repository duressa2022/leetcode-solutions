class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter=Counter(nums)
        values=counter.values()
        maxValue=max(values)
        counter=0
        for value in values:
            if value==maxValue:
                counter+=1
        return maxValue*counter

        