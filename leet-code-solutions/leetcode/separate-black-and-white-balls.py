class Solution:
    def minimumSteps(self, s: str) -> int:
        result,countOnes=0,0
        for bit in  s:
            if bit=="1":
                countOnes+=1
            else:
                result+=countOnes
        return result

        


        