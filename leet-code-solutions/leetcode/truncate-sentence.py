class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls_word=s.split()
        result=[]
        for i in range(k):
            result.append(ls_word[i])
        return " ".join(result)
        