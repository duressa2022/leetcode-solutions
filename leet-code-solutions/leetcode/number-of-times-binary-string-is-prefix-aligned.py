class Solution:
  def numTimesAllBlue(self, flips: List[int]) -> int:
    result = 0
    right = 0

    for i, flip in enumerate(flips):
      right = max(right, flip)
      if right == i + 1:
        result += 1

    return result