from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result=[]
        hash_map=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hash_map[i+j].append(mat[i][j])
        for key in hash_map:
            if key%2==1:
                result+=hash_map[key]
            else:
                result+=hash_map[key][::-1]
        return result


        