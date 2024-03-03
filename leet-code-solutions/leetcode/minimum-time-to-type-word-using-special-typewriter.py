class Solution:
    def minTimeToType(self, word: str) -> int:
        counter=0
        current="a"
        for char in word:
            maxValue=min((ord(char)-ord(current))%26,26-(ord(char)-ord(current))%26)
            counter+=maxValue+1
            current=char
        return counter

        