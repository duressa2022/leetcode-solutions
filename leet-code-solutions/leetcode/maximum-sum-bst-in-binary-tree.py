# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def check(node,leftMax,rightMin):
            if leftMax>=node.val or rightMin<=node.val:
                return False
            return True
        def helperFunction(node,ans):
            if not node:
                return [0,float("inf"),-float("inf")]

            leftSum,leftMin,leftMax=helperFunction(node.left,ans)
            rightSum,rightMin,rightMax=helperFunction(node.right,ans)

            if leftSum!="a" and rightSum!="a" and check(node,leftMax,rightMin):
                current=leftSum+rightSum+node.val
                currentMin=min(leftMin,rightMin,node.val)
                currentMax=max(leftMax,rightMax,node.val)
                ans[0]=max(ans[0],current)
                return [current,currentMin,currentMax]
            return ["a",node.val,node.val]

        ans = [0]
        helperFunction(root, ans)
        return ans[0]