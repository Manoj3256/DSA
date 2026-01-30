# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        first=[]
        second=[]
        def bfs(root,level,lis):
            if len(lis)==level:
                lis.append([])
            if not root:
                lis[level].append(None)
                return 
            lis[level].append(root.val)
            bfs(root.left,level+1,lis)
            bfs(root.right,level+1,lis)
        bfs(p,0,first)
        bfs(q,0,second)
        return first==second
