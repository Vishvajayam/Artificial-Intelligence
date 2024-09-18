class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def bfs_binary_tree(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=' ')
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

if __name__ == "__main__":
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("\nBFS Traversal of Binary Tree:")
    bfs_binary_tree(root)
