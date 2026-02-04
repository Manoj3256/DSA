# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        def bfs(root,result,level,choice):
            if not root:
                return 
            if len(result)==level:
                result.append([])
            if choice==1:
                result[level].insert(0,root.val)
            else:
                result[level].append(root.val)
            bfs(root.left,result,level+1,1-choice)
            bfs(root.right,result,level+1,1-choice)
        bfs(root,result,0,0)
        return result