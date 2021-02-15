# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val == p.val or root.val == q.val:
            return root
        
        big_num = max(p.val, q.val)
        small_num = min(p.val, q.val)
        
        if big_num > root.val and small_num > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif big_num < root.val and small_num < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

            