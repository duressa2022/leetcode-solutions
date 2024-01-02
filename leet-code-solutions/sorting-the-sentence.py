class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(" ")
        result=[""]*len(words)
        for word in words:
            result[int(word[-1])-1]=word[:len(word)-1]
        return " ".join(result)
        