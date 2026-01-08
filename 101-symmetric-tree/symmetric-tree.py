# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mirrorcheck(ele1,ele2):
            if not ele1 and not ele2:
                return True
            if not ele1 or not ele2:
                return False
            return  ele1.val==ele2.val and mirrorcheck(ele1.left,ele2.right) and mirrorcheck(ele1.right,ele2.left)
        return mirrorcheck(root.left,root.right)
