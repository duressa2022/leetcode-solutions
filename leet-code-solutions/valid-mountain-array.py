class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:return False
        changeFinder=0
        isChanged=False
        while changeFinder<len(arr)-1:
            if arr[changeFinder]<arr[changeFinder+1]:
                changeFinder+=1
            else:
                isChanged=True
                break
        if isChanged==False or changeFinder==0:
            return False
        while changeFinder<len(arr)-1:
            if arr[changeFinder]>arr[changeFinder+1]:
                changeFinder+=1
            else:
                break
        return True if changeFinder==len(arr)-1  else False

        