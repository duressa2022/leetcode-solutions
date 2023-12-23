class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result=[]
        i=0
        j=len(nums)//2
        while i<j and j<len(nums):
            result.append(nums[i])
            result.append(nums[j])
            i=i+1
            j=j+1
        return result

        