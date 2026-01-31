# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        dic={}
        def binary(root,dic,k):
            if not root:
                return 
            dic[root.val]=k-root.val
            binary(root.left,dic,k)
            binary(root.right,dic,k)
        binary(root,dic,k)
        for i,j in dic.items():
            if j in dic and j!=i:
                return True
        return False