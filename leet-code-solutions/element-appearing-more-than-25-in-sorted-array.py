class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length=len(arr)//4
        hash_map={}
        for i in range(len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]]=1
            else:
                 hash_map[arr[i]]+=1
        for value in hash_map:
            if hash_map[value]>length:
                return value


        