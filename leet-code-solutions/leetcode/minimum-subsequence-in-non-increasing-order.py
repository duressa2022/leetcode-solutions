class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        result=[]
        nums.sort(reverse=True)
        total=sum(nums)
        current=0
        for num in nums:
            current+=num
            result.append(num)
            if current>total-current:
                return result
        return result

        