class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=sum([value for value in range(1,n+1) if value%m!=0])
        num2=sum([value for value in range(1,n+1) if value%m==0])
        return num1-num2

        