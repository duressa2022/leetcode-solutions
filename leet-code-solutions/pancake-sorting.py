class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sorted_number=[number for number in arr]
        sorted_number.sort()
        last_index=len(arr)-1
        result=[]
        k_maxNumber=1
        while sorted_number!=arr:
            max_index=arr.index(max(arr[:last_index+1]))
            self.revList(arr,0,max_index)
            result.append(max_index+1)
            self.revList(arr,0,last_index)
            result.append(last_index+1)
            last_index=last_index-1
            k_maxNumber+=1
        return result
        
    def revList(self,array,left,right):
        while left<right:
            (array[left],array[right])=(array[right],array[left])
            left=left+1
            right=right-1
