class Solution:
    def numberOfWays(self, s: str) -> int:
        length=len(s)
        one_zero=[0]*length
        zero_one=[0]*length
        future_one=[0]*length
        future_zero=[0]*(length)
        prev_zero=0
        for i in range(length):
            if s[i]=="0":
                prev_zero+=1
            else:
                one_zero[i]=prev_zero
        count_zero=s.count("0")
        for i in range(length):
            if s[i]=="0":
                count_zero-=1
                future_zero[i]=count_zero
            else:
                future_zero[i]=count_zero
        prev_one=0
        for i in range(length):
            if s[i]=="1":
                prev_one+=1
            else:
                zero_one[i]=prev_one
        count_one=s.count("1")
        for i in range(length):
            if s[i]=="1":
                count_one-=1
                future_one[i]=count_one
            else:
                future_one[i]=count_one
        result=0
        for i in range(length):
            first=one_zero[i]*future_zero[i]
            second=zero_one[i]*future_one[i]
            result+=first+second
        return result
        
    
        