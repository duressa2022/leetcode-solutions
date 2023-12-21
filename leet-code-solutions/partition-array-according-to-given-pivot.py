class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums=[i for i in nums if i<pivot]+[i for i in nums if i==pivot]+[i for i in nums if i>pivot]
        return nums
        