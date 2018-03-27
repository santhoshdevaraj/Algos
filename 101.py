# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetry(root1, root2):
        	if not root1 and not root2:
        		return True
        	if not root1 or not root2 or root1.val != root2.val:
        		return False
        	return symmetry(root1.left, root2.right) and symmetry(root1.right, root2.left)

      	return symmetry(root, root)
