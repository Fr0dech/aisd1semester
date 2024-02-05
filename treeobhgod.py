class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(tree_string):
    stack = []
    node = None
    for char in tree_string:
        if char == "(":
            stack.append(node)
        elif char == ")":
            node = stack.pop()
        elif char != ",":
            node = Node(char)
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
        else:
            continue

    return node

def preorder_traversal(node):
    if node is None:
        return

    print(node.value, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node.value, end=" ")
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end=" ")

# Ввод строки в линейно-скобочной записи
tree_string = "8(3(1,6(4,7)),2(,5(9,)))"

# Создание дерева
root = create_tree(tree_string)

# Прямой обход
print("Прямой обход (префиксный):")
preorder_traversal(root)
print("\n")

# Центровой обход
print("Центровой обход (инфиксный):")
inorder_traversal(root)
print("\n")

# Концевой обход
print("Концевой обход (постфиксный):")
postorder_traversal(root)
print("\n")