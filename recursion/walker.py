# walker.py

def print_tree(node, depth=0):
    space = depth * '   '
    for item in node:
        if isinstance(item, tuple):
            print(space, item[0])
            print_tree(item[1], depth + 1)
        else:
            print(space, item)
