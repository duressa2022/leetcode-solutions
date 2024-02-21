class Solution:
    def minimumSum(self, num: int) -> int:
        numbers=sorted(str(num))
        return int(numbers[0]+numbers[-1])+int(numbers[1]+numbers[-2])

        