class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_number=max(nums)
        result=0
        score=max_number
        for i in range(k):
            result+=score
            score=score+1
        return result
        