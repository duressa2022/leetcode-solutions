class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter=Counter(s)
        maxLength=0
        oddFinder=False
        for char in counter:
            if counter[char]%2==1:
                oddFinder=True
        for char in counter:
            if counter[char]%2==0:
                maxLength+=counter[char]
            else:
                maxLength+=counter[char]-1  
        return maxLength if not oddFinder else maxLength+1


        