class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length=-float("inf")
        for sentence in sentences:
            max_length=max(max_length,len(sentence.split()))
        return max_length

        