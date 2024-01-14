class Solution:
    def smallestNumber(self, number: int) -> int:
        result="0"
        if number>0:
            ls_number=[int(value) for value in str(number)]
            ls_number.sort()
            if ls_number[0]==0:
                for i in range(len(ls_number)):
                    if ls_number[i]!=0:
                        (ls_number[0],ls_number[i])=(ls_number[i],ls_number[0])
                        break
            result="".join([str(value) for value in ls_number])
        else:
            ls_number=[int(value) for value in str(-number)]
            ls_number.sort(reverse=True)
            result="".join([str(value) for value in ls_number])
        return int(result) if number>0 else -int(result)
            

    
        