class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    total = sum(nums)
    remainder = total % p
    if remainder == 0:
      return 0

    result = len(nums)
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      prefix %= p
      target = (prefix - remainder + p) % p
      if target in prefixToIndex:
        result = min(result, i - prefixToIndex[target])
      prefixToIndex[prefix] = i

    return -1 if result == len(nums) else result   