class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        length=len(nums)
        counter=0
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        counter+=1
        return counter
        