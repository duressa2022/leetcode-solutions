# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helperFunction(array):
            maxValue=-float("inf")
            index=0
            for i in range(len(array)):
                if maxValue<array[i]:
                    maxValue=array[i]
                    index=i
            return index
        if not nums:
            return None
        index=helperFunction(nums)
        root=TreeNode(nums[index])
        root.left=self.constructMaximumBinaryTree(nums[:index])
        root.right=self.constructMaximumBinaryTree(nums[index+1:])
        return root
    
        