# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def depth(root,sum):
            if not root:
                return 0
            sum=sum*10+root.val
            if not root.left and not root.right:
                return sum
            return depth(root.left,sum)+depth(root.right,sum)
        
        return depth(root,0)