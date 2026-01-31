# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res=[]
        def bfs(root,level,res):
            if not root:
                return 
            if len(res)==level:
                res.append([])
            res[level].append(root.val)
            bfs(root.left,level+1,res)
            bfs(root.right,level+1,res)
        bfs(root,0,res)
        for i in range(len(res)):
            res[i]=sum(res[i])/float(len(res[i]))
        return res
