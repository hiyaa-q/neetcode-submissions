# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculateDepth(root: Optional[TreeNode], currentDepth) -> int:
            if root == None: return currentDepth;
            currentDepth += 1
            return max(calculateDepth(root.left, currentDepth), calculateDepth(root.right, currentDepth))
        
        return calculateDepth(root, 0)
        