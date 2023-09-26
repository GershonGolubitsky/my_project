class TreeNode:
    """The largest query sequence in a binary tree"""

    def __init__(self, value, left=None, right=None):
        # Constructor of a single node
        self.value = value
        self.left = left
        self.right = right

def zigzag(node, orientation):
    # If the node has no sons, you have reached the end of the tree
    if not node:
        return -1
    # If there was a zigzag from the left,
    # you will send a recursion to the same function if there is a right pointer
    left = zigzag(node.left, 'right')
    # If there was a zigzag from the right,
    # you will send a recursion to the same function if there is a left pointer
    right = zigzag(node.right, 'left')
    # Returns the largest value between left side and right side
    if orientation == "right":
        return max(left, right + 1)
    else:
        return max(left + 1, right)


def max_tree(random_tree):
    right, left = 0, 0
    # If first pointer will be on the left side
    if random_tree.right:
        orientation = "left"
        right = zigzag(random_tree.right, orientation)
    # If first pointer will be on the right side
    if random_tree.left:
        orientation = "right"
        left = zigzag(random_tree.left, orientation)
    # Returns the largest query sequence
    return max(left, right)
