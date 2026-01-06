# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def level(root,l):
            if not root:
                return 
            if len(res)==l:
                res.append([])
            res[l].append(root.val)
            level(root.left,l+1)
            level(root.right,l+1)
        res=[]
        level(root,0)
        return res