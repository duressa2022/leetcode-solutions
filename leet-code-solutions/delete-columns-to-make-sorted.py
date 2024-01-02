class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        list_string=[list(string) for string in strs]
        counter=0
        for i in range(len(list_string[0])):
            for j in range(len(list_string)-1):
                if list_string[j][i]>list_string[j+1][i]:
                    counter+=1
                    break
        return counter
        