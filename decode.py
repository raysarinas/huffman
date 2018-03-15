# MAYBE THIS

def decode (tree, bitreader):
    while True:
        if isinstance(tree, TreeLeafEndMessage):
            return None
        elif isinstance(tree, TreeLeaf):
            return tree.value
        elif isinstance(tree, TreeBranch):
            if bitreader.readbit() == 0:
                tree = tree.left
            else:
                tree = tree.right
        else:
            raise TypeError('{} is not a tree type'.format(type(tree)))
