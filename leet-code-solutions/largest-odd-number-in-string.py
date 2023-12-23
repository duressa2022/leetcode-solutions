class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        number=int(num)
        while number>0:
            if number%2==1:
                return str(number)
            number//=10
        return ""
        