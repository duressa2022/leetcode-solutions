class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hash_map={char:i for i,char in enumerate(order)}
        result=[]
        for word in words:
            temp=[]
            for char in word:
                temp.append(hash_map[char])
            result.append(temp)
        for i in range(len(result)-1):
            if result[i]>result[i+1]:
                return False
        return True

            
        