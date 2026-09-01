# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxp=root.val

        def dfs(node):
            nonlocal maxp
            if not node:
                return 0
            
            right=dfs(node.right)
            left=dfs(node.left)
            leftMax=max(left,0)
            rightMax=max(right ,0)

            maxp=max(maxp,node.val + rightMax+leftMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return maxp

