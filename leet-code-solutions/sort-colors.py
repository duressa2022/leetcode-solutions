class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer=-1
        onePointer=-1
        twoPointer=-1
        for num in nums:
            if num==0:
                zeroPointer+=1
                onePointer+=1
                twoPointer+=1
                nums[twoPointer]=2
                nums[onePointer]=1
                nums[zeroPointer]=0
            elif num==1:
                onePointer+=1
                twoPointer+=1
                nums[twoPointer]=2
                nums[onePointer]=1
            else:
                twoPointer+=1
                nums[twoPointer]=2
        


        