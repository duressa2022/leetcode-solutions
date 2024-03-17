class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter=Counter(nums)
        result=0
        for num in nums:
            if counter[num]==1:
                result+=num
        return result
            
