# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def depth_check(node) :
            if not node:
                return 0
            left = depth_check(node.left)
            if left == -1:
                return -1
            right = depth_check(node.right)
            if right == -1:
                return -1
            if 1<abs(left-right):
                print("False graph")
                return -1
            return 1+max(left, right)
        return depth_check(root)!=-1
