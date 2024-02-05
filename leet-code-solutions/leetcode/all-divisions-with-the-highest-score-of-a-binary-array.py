class Solution:
  def maxScoreIndices(self, nums: List[int]) -> List[int]:
    zeros = nums.count(0)
    ones = len(nums) - zeros
    result = [0] 
    left_zeros = 0
    left_ones = 0
    max_score = ones

    for i, num in enumerate(nums):
      left_zeros += num == 0
      left_ones += num == 1
      right_ones = ones - left_ones
      score = left_zeros + right_ones
      if max_score == score:
        result.append(i + 1)
      elif max_score < score:
        max_score = score
        result = [i + 1]

    return result



            

        