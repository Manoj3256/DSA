# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        if root is None:
            return []
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)
        return res
        