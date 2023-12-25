class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        string1="qwertyuiop"
        string2="asdfghjkl"
        string3="zxcvbnm"
        result=[]
        for word in words:
            item=word.lower()
            if self.checkString(item,string1) or self.checkString(item,string2) or self.checkString(item,string3):
                result.append(word)
        return result

    def checkString(self,word,string):
        for char in word:
            if char not in string:
                return False
        return True
       



        