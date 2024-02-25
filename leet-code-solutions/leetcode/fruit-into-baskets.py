class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter=defaultdict(int)
        left,right,length=0,0,len(fruits)
        result=-1
        while right<length:
            counter[fruits[right]]+=1
            if len(counter)>2:
                result=max(result,right-left)
                counter[fruits[left]]-=1
                if counter[fruits[left]]==0:
                    del counter[fruits[left]]
                left=left+1
            right=right+1
        return max(right-left,result)



        



