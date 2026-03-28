# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not preorder:
            return None
        root=TreeNode(preorder[0])
        ind=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:ind+1],inorder[:ind])
        root.right=self.buildTree(preorder[ind+1:],inorder[ind+1:])
        return root