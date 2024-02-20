class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countFive=0
        countTen=0
        for bill in bills:
            if bill==5:
                countFive+=1
            elif bill==10:
                countFive-=1
                countTen+=1
            elif countTen>0:
                countFive-=1
                countTen-=1
            else:
                countFive-=3

            print(countFive)
            if countFive<0:
                return False
        return True
        