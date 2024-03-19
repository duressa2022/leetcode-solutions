class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters="abcdefghijklmnopqrstuvwxyz"
        morse_map={}
        for i in range(26):
            morse_map[letters[i]]=code[i]
        result_set=set()
        for word in words:
            decoder=""
            for char in word:
                decoder+=morse_map[char]
            result_set.add(decoder)
        return len(result_set)
        