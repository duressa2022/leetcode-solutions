class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        total_even= 0
        for value in nums:
            if value%2==0:
                total_even+=value
        for value, index in queries:
            if nums[index] % 2 == 0:
                total_even =total_even- nums[index]
            nums[index] =nums[index]+ value
            if nums[index] % 2 == 0:
                total_even =total_even+nums[index]
            result.append(total_even)
        return result


        

        