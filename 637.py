# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue, output = [root], []

        while queue:
            output.append(sum(node.val for node in queue)/float(len(queue)))
            queue = filter(None, (node for root in queue for node in (root.left, root.right)))

        return output

