class Solution:
    def minimizedStringLength(self, string: str) -> int:
        hash_set={char for char in string}
        return len(hash_set)
       
        

        