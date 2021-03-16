class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
    	if not root:
    		return 0

    	queue = deque([root])
    	answer = 0

    	while queue:
    		answer += 1
    		for _ in range(len(queue)):
    			curr = queue.popleft()

    			if curr.right:
    				queue.append(curr.right)
    			if curr.left:
    				queue.append(curr.left)
    	
    	return answer

sample1 = TreeNode(5,None,None)
sample2 = TreeNode(4,None,None)
sample3 = TreeNode(2, sample2, None)
sample4 = TreeNode(3,None,sample1)
sample5 = TreeNode(1,sample3, sample4)

sample6 = TreeNode(0, None,None)

print(Solution.maxDepth(None,sample5))