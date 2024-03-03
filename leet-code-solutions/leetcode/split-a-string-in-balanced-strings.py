class Solution:
    def balancedStringSplit(self, s: str) -> int:
        numberR=0
        numberL=0
        counter=0
        for char in s:
            if char=="R":
                numberR+=1
            if char=="L":
                numberL+=1
            if numberR==numberL:
                counter+=1
                numberR=0
                numberL=0
        return counter

        