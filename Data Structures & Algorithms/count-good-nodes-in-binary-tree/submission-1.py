# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res=[]
        
        def dfs(node,maxp):
            if not node:
                return None
            if node.val>=maxp:
                res.append(node.val)
                maxp=node.val
            dfs(node.right,maxp)
            dfs(node.left,maxp)
        
        dfs(root,root.val)
        return len(res)


        