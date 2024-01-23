class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap=defaultdict(int)
        length=len(s)
        left,right=0,10
        result=[]
        print(len(s))
        while right<len(s)+1:
            hashMap[s[left:right]]+=1
            if hashMap[s[left:right]]>=2:
                result.append(s[left:right])
                hashMap[s[left:right]]-=length
            left=left+1
            right=right+1
        print(hashMap)
        return result



            

        