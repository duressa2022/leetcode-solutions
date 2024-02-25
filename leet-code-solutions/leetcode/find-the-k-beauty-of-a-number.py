class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        number=num
        left=0
        right=k
        strNumber=str(num)
        counter=0
        while right<len(strNumber)+1:
            temp=strNumber[left:right]
            temp=int(temp)
            if  temp!=0 and number%temp==0:
                counter+=1
            left=left+1
            right=right+1
        return counter

            


        

        