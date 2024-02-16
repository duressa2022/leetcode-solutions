class Solution:
  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    result = 0
    maxCount = 0
    counter = Counter()

    l = 0
    for r, c in enumerate(answerKey):
      counter[c == 'T'] += 1
      maxCount = max(maxCount, counter[c == 'T'])
      while maxCount + k < r - l + 1:
        counter[answerKey[l] == 'T'] -= 1
        l += 1
      result = max(result, r - l + 1)

    return result