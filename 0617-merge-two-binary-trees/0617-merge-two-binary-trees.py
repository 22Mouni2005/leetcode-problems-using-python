# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(r1,r2):
            if r1 is None and r2 is None:
                return None
            if r1 is None and r2:
                return r2
            if r2 is None and r1: 
                return r1
            new_val=r1.val+r2.val
            new_root=TreeNode(new_val)
            new_root.left=merge(r1.left,r2.left)
            new_root.right=merge(r1.right,r2.right)
            return new_root
        return merge(root1,root2)

        