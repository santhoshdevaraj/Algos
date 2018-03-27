# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
# then sum node values up as the new value of the merged node. Otherwise, the NOT null 
# node will be used as the node of new tree.

# Example 1:
# Input: 
#   Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
#        3
#       / \
#      4   5
#     / \   \ 
#    5   4   7
# Note: The merging process must start from the root nodes of both trees.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1_node1 = TreeNode(1)
t1_node2 = TreeNode(2)
t1_node3 = TreeNode(3)
t1_node5 = TreeNode(5)

t2_node1 = TreeNode(1)
t2_node2 = TreeNode(2)
t2_node3 = TreeNode(3)
t2_node4 = TreeNode(4)
t2_node7 = TreeNode(7)

t1_node1.left = t1_node3
t1_node1.right = t1_node2
t1_node3.left = t1_node5

t2_node2.left = t2_node1
t2_node2.right = t2_node3
t2_node1.right = t2_node4
t2_node3.right = t2_node7


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return

        root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))

        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        
        return root

root = Solution().mergeTrees(t1_node1, t2_node2)
