class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * (len(nums) +1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        #calculation part
        answer = []
        len_nums = len(nums)
        for i in range(len(nums)):
            # left side calculated result
            left = (nums[i] * i) - prefix_sum[i]
            # right side elements sum
            right_sum = prefix_sum[-1] - prefix_sum[(i+1)%len(prefix_sum)]
            # right side calculated result
            right =  right_sum - nums[i] * (len(nums) - (i+1))

            answer.append(right+left)
        return answer