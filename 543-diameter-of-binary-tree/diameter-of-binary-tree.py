# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        height(root)
        return self.ans
