# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ld = 0
        self.heightAtCurrentNode(root)
        return self.ld

    def heightAtCurrentNode(self, node):

        if not node:
            return 0
            
        left = self.heightAtCurrentNode(node.left)
        right = self.heightAtCurrentNode(node.right)

        self.ld = max(left + right, self.ld)

        return 1 + max(left, right)