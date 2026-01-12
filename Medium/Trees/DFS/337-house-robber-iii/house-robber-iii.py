# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def robert(root):
            if not root:
                return (0,0)
            left=robert(root.left)
            right=robert(root.right)
            skip=max(left)+max(right)
            money=root.val+left[1]+right[1]
            return (money,skip)
        return max(robert(root))

            