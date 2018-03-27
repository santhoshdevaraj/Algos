# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        queue, output = [root] if root else [], []
        
        while queue:
            output.append(max(node.val for node in queue))
            queue = filter(None, [node for root in queue for node in [root.left, root.right]])

        return output
