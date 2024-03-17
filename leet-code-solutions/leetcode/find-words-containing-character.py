class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i in range(len(words)):
            for char in words[i]:
                if char==x:
                    result.append(i)
                    break
        return result