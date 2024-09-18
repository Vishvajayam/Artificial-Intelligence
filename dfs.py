class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def dfs_binary_tree(node):
    if node is None:
        return
    print(node.value, end=' ')
    dfs_binary_tree(node.left)
    dfs_binary_tree(node.right)

if __name__ == "__main__":
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("\nDFS Traversal of Binary Tree:")
    dfs_binary_tree(root)
