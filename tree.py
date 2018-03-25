

#    1
#  /   \
# 2     3
#  \   /
#   5 4

# Definition for a binary tree node.

class Node(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def mktree():
    five  = Node(5)
    four  = Node(4)
    six   = Node(6)
    two   = Node(2, six, five)
    three = Node(3, four, None)
    one   = Node(1, two, three)
    
    return one

root = mktree()
