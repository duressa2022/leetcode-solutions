class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [] if (num-3)%3!=0 else [int((num-3)/3),int((num-3)/3)+1,int((num-3)/3)+2]
        