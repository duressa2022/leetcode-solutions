class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringNumber=int("".join([str(digit) for digit in digits]))
        stringNumber=stringNumber+1
        return [int(number) for number in str(stringNumber)]
        