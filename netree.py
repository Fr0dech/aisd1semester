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

def iterative_preorder_traversal(root):
    if root is None:
        return ""

    stack = []
    result = ""
    stack.append(root)

    while stack:
        node = stack.pop()
        result += str(node.value) + " "

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result.strip()

# Ввод строки в линейно-скобочной записи
tree_string = "8(3(1,6(4,7)),2(,5(9,)))"

# Создание дерева
root = create_tree(tree_string)

# Нерекурсивный прямой обход
result = iterative_preorder_traversal(root)

# Вывод результата
print("Нерекурсивный прямой обход:")
print(result)