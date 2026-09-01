# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c=k
        res=root.val
        def dfs(node):
            nonlocal c,res
            if not node :
                return
            dfs(node.left)
            c-=1
            if c==0:
                res= node.val
            dfs(node.right)

        dfs(root)
        return res
