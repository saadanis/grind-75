# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            root = self.invertChildren(root)
    
        return root

    def invertChildren(self, node):

        temp = node.left
        node.left = node.right
        node.right = temp

        if node.left:
            node.left = self.invertChildren(node.left)
        
        if node.right:
            node.right = self.invertChildren(node.right)
        
        return node