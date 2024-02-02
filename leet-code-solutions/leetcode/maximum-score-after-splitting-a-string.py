class Solution:
    def maxScore(self, s: str) -> int:
        length=len(s)
        left=[0]*(length+1)
        for i in range(1,length+1):
            if s[i-1]=="0":
                left[i]=left[i-1]+1
            else:
                left[i]=left[i-1]
        right=[0]*(length+1)
        for i in range(length-1,-1,-1):
            if s[i]=="1":
                right[i]+=right[i+1]+1
            else:
                right[i]=right[i+1]
        print(left)
        print(right)
        score=0
        left.pop(0)
        right.pop()
        for i in range(length-1):
            score=max(score,left[i]+right[i+1])
        return score

        