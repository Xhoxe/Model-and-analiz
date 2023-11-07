class task2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: task2):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return inorder(root)

node3 = task2(3)
node2 = task2(2, left=node3)
root = task2(1, right=node2)

print(inorderTraversal(root))