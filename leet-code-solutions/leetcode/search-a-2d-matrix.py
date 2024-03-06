class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #better case 
        createdList=[]
        for row in matrix:
            createdList.extend(row)
        left,right=0,len(createdList)-1
        while left<=right:
            mid=(left+right)//2
            if createdList[mid]==target:
                return True
            elif createdList[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
    
        #brute force method
        def helperFunction(array,target):
            left,right=0,len(array)-1
            while left<=right:
                mid=(left+right)//2
                if array[mid]==target:
                    return True
                elif array[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return False
        for array in matrix:
            if helperFunction(array,target):
                return True
        return False
        