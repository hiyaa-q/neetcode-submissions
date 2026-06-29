# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, root_height):
            if (root == None):
                return [root_height, True]

            leftResult = dfs(root.left, root_height+1)
            rightResult = dfs(root.right, root_height+1)

            return [max(leftResult[0], rightResult[0]), (leftResult[1] and rightResult[1] and abs(leftResult[0] - rightResult[0]) < 2)]

        return dfs(root, 0)[1]