# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def createTree(array):
            if not array:return None
            mid=len(array)//2
            root=TreeNode(array[mid])
            root.left=createTree(array[:mid])
            root.right=createTree(array[mid+1:])
            return root
        array=self.linkedlistTo(head)
        return createTree(array)

    def linkedlistTo(self,head):
        result=[]
        current=head
        while current:
            result.append(current.val)
            current=current.next
        return result
        