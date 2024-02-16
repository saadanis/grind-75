# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val or root.val == q.val:
            return root
        
        while root:
            root_val = root.val
            if root_val < p.val and root_val < q.val:
                root = root.right
            elif root_val > p.val and root_val > q.val:
                root = root.left
            else:
                return root
        
        return root
        