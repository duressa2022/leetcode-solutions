class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row_length=len(mat)
        ones=0
        index=0
        for i in range(row_length):
            counter=0
            for num in mat[i]:
                if num==1:
                    counter+=1
            if counter>ones:
                ones=counter
                index=i
            else:
                if counter==ones:
                    index=min(index,i)
        return [index,ones]
        