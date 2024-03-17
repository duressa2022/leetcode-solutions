class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        length=len(heights)
        counter=0
        for i in range(length):
            if expected[i]!=heights[i]:
                counter+=1
        return counter
        