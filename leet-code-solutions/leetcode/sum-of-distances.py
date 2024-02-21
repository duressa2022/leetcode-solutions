class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        count_number_left=defaultdict(int)
        sum_index_left=defaultdict(int)
        leftFrqCounter=[0]*len(nums)
        for index,value in enumerate(nums):
            leftFrqCounter[index]=count_number_left[value]
            count_number_left[value]+=1
        leftIndexSumCounter=[0]*len(nums)
        for index,value in  enumerate(nums):
            leftIndexSumCounter[index]+=sum_index_left[value]
            sum_index_left[value]+=index
        count_number_right=defaultdict(int)
        rightFrqCounter=[0]*len(nums)
        for index,value in enumerate(reversed(nums)):
            rightFrqCounter[index]=count_number_right[value]
            count_number_right[value]+=1
        rightFrqCounter.reverse()

        rightIndexSumCounter=[0]*len(nums)
        sum_index_right=defaultdict(int)
        for index,value in enumerate(reversed(nums)):
            rightIndexSumCounter[index]=sum_index_right[value]
            sum_index_right[value]+=len(nums)-index-1
        rightIndexSumCounter.reverse()
        for index,value in enumerate(nums):
            leftResult=leftFrqCounter[index]*index-leftIndexSumCounter[index]
            rightResult=rightIndexSumCounter[index]-rightFrqCounter[index]*index
            result[index]=leftResult+rightResult
        return result



        