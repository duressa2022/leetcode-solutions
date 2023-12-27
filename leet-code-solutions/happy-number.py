class Solution:
    def isHappy(self, number: int) -> bool:
         hash_set=set()
         hash_set.add(1)
         while number not in hash_set:
            hash_set.add(number)
            number=sum([int(i)**2 for i in str(number)])
         return number==1
        