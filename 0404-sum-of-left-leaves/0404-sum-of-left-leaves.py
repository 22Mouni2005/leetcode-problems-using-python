# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leafleft(node):
            if node is None:
                return 0
            if node.left and node.left.left is None and node.left.right is None:
                return node.left.val+leafleft(node.right)
            return leafleft(node.left)+leafleft(node.right)
        return leafleft(root)
        

        