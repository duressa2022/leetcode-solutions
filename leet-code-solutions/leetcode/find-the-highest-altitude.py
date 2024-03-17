class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result=0
        total=0
        for i in range(len(gain)):
            total+=gain[i]
            result=max(result,total)
        return result
        