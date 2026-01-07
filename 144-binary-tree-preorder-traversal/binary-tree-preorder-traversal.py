# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def order(root):
            if not root:
                return []
            res.append(root.val)
            order(root.left)
            order(root.right)
        res=[]
        order(root)
        return res