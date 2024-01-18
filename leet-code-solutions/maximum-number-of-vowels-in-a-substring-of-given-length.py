class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hash_set={"a","e","i","o","u"}
        temp_counter=[0]*(len(s)+1)
        for i in range(1,len(s)+1):
            if s[i-1] not in hash_set:
                temp_counter[i]=temp_counter[i-1]
            else:
                temp_counter[i]=temp_counter[i-1]+1
        left,right=0,k
        counter=0
        while right<len(s)+1:
            current=temp_counter[right]-temp_counter[left]
            counter=max(counter,current)
            left=left+1
            right=right+1
        return counter

       
        return 0
