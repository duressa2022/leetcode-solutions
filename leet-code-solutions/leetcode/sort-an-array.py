class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return self.mergeArray(left,right)
    def mergeArray(self,array1,array2):
        array=[]
        i=j=0
        while i<len(array1) and j<len(array2):
            if array1[i]<array2[j]:
                array.append(array1[i])
                i=i+1
            else:
                array.append(array2[j])
                j=j+1
        while i<len(array1):
            array.append(array1[i])
            i=i+1
        while j<len(array2):
            array.append(array2[j])
            j=j+1
        return array

        