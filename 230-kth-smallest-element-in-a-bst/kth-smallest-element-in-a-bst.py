# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.ans
