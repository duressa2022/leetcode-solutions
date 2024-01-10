import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        possibleNumber=[number for number in range(math.floor(math.sqrt(c))+1)]
        left=0
        right=len(possibleNumber)-1
        while left<=right:
            current=possibleNumber[left]**2+possibleNumber[right]**2
            if current==c:
                return True
            elif current>c:
                right=right-1
            else:
                left=left+1
        return False

        