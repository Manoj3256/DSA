# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.maxc=self.count=0
        self.mode=[]
        self.prev=None
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            if self.prev==root.val:
                self.count+=1
            else:
                self.count=1
            if self.count>self.maxc:
                self.maxc=self.count
                self.mode=[root.val]
            elif self.count==self.maxc:
                self.mode.append(root.val)
            self.prev=root.val
            dfs(root.right)
        dfs(root)
        return self.mode