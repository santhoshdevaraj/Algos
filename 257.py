# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

from tree import root

class Solution(object):
    def __init__(self):
        self.array = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        
        if not root.left and not root.right: return ['%s' %(root.val)]
        
        return ['%s->%s' %(root.val, i) for i in self.binaryTreePaths(root.left)] + ['%s->%s' %(root.val, i) for i in self.binaryTreePaths(root.right)]


print Solution().binaryTreePaths(root)