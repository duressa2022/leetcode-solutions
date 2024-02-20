class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        score=0
        while target>1:
            if target%2==1:
                target-=1
            else:
                if maxDoubles>0:
                    target//=2
                    maxDoubles-=1
                else:
                    target-=1
            score=score+1
            if maxDoubles==0:
                return score+target-1
        return score
        