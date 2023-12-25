class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length=-float("inf")
        ls_string=s.split()
        result=[]
        for word in ls_string:
            length=max(length,len(word))
        for i in range(length):
            temp=""
            for word in ls_string:
                if i>=len(word):
                    temp+=" "
                else:
                    temp+=word[i]
            temp=temp.rstrip()
            result.append(temp)
        return result


        
        

        