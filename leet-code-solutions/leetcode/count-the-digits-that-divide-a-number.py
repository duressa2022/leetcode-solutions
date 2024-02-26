class Solution:
    def countDigits(self, num: int) -> int:
        number=list(str(num))
        counter=0
        for value in number:
            if num%int(value)==0:
                counter+=1
        return counter
        