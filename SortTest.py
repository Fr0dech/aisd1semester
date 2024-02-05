class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root, sorted_arr):
    if root:
        inorder_traversal(root.left, sorted_arr)
        sorted_arr.append(root.value)
        inorder_traversal(root.right, sorted_arr)
    return sorted_arr

def bst_sort(arr):
    root = None
    for value in arr:
        root = insert(root, value)
    sorted_arr = inorder_traversal(root, [])
    return sorted_arr

arr = [5, 3, 8, 6, 2, 7, 1, 4]
sorted_arr = bst_sort(arr)
print(sorted_arr)