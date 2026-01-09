# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def pathsum(root,target,curr):
            if not root:
                return False
            if not root.left and not root.right and curr+root.val==target:
                return True
            return pathsum(root.left,target,curr+root.val) or pathsum(root.right,target,curr+root.val)
        return pathsum(root,targetSum,0)