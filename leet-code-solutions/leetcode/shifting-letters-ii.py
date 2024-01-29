class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        listString=[0]*((len(s)))
        for shift in shifts:
            left,right,k=shift
            if k==1:
                listString[left]+=1
                if right+1<len(s):
                    listString[right+1]+=-1
            else:
                listString[left]+=-1
                if right+1<len(s):
                    listString[right+1]+=1
        running=0
        for i in range(len(s)):
            running+=listString[i]
            listString[i]=running
        result=""
        for index in range(len(s)):
            temp=chr((ord(s[index])-ord("a")+listString[index])%26+ord("a"))
            result+=temp
        return result
            
