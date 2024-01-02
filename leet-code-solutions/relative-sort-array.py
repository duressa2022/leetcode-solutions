class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map={number:index for index,number in enumerate(arr2)}
        holder=-1
        for seeker in range(0,len(arr1)):
            if arr1[seeker] in hash_map:
                holder+=1
                (arr1[seeker],arr1[holder])=(arr1[holder],arr1[seeker])
        for i in range(len(arr1)):
            for j in range(len(arr1)-1):
                if arr1[j] in hash_map and arr1[j+1] in hash_map:
                    if hash_map[arr1[j]]>hash_map[arr1[j+1]]:
                        (arr1[j],arr1[j+1])=(arr1[j+1],arr1[j])
                elif arr1[j] not in hash_map and arr1[j+1] not in hash_map:
                    if arr1[j]>arr1[j+1]:
                        (arr1[j],arr1[j+1])=(arr1[j+1],arr1[j])
        return arr1


            