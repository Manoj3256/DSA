# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result,string=[],''
        def bfs(root,result,string):
            if not string:
                string+=str(root.val)
            else:
                string+="->"+str(root.val)
            if not root.left and not root.right:
                result.append(string)
                return
            if root.left:
                bfs(root.left,result,string)
            if root.right:
                bfs(root.right,result,string)
        bfs(root,result,string)
        return result
            
