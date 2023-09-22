class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.counter_l = 0
        self.counter_r = 0


def zigzag(node, orientation):
    if not node:
        return -1

    left = zigzag(node.left, 'right')
    right = zigzag(node.right, 'left')
    if orientation == "right":
        return max(left, right + 1)
        # lz = max(left, right + 1)
    else:
        return max(left + 1, right)
        # lz = max(left + 1, right)
    #print(lz, node.value)
    #return lz


def max_tree(random_tree):
    right, left = 0, 0
    if random_tree.right:
        orientation = "left"
        right = zigzag(random_tree.right, orientation)
    if random_tree.left:
        orientation = "right"
        left = zigzag(random_tree.left, orientation)
    return max(left, right)
