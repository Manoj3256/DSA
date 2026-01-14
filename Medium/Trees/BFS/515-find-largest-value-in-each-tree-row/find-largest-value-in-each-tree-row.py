# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        def bfs(root,result,level):
            if not root:
                return
            if level==len(result):
                result.append(root.val)
            elif result[level]<root.val:
                result[level]=root.val
            bfs(root.left,result,level+1)
            bfs(root.right,result,level+1)
        bfs(root,result,0)
        return result