import re

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

def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def print_bst(root):
    if root is not None:
        print(f"{root.value}", end='')
        if root.left or root.right:
            print(" (", end='')
            print_bst(root.left)
            if root.right:
                print(", ", end='')
            print_bst(root.right)
            print(")", end='')



def build_binary_tree(tree_string):
    stack = []
    node = None
    value = ''
    for char in tree_string:
        if char == "(":
            stack.append(node)
        elif char == ")":
            node = stack.pop()
        elif char != "," and char != " ":
            value += char
            continue
        if value:
            node = Node(int(value))
            value = ''
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

    return node

tree_string = "8 (3 (1, 6 (4,7)), 2 (, 5(9,)))"
bst = build_binary_tree(tree_string)

while True:
    print("Меню:")
    print("1. Добавить вершину")
    print("2. Удалить вершину")
    print("3. Найти вершину")
    print("4. Вывести БДП")
    print("5. Выход")
    choice = input("Выберите операцию (1-5): ")

    if choice == "1":
        value = int(input("Введите значение вершины для добавления: "))
        bst = insert(bst, value)
    elif choice == "2":
        value = int(input("Введите значение вершины для удаления: "))
        bst = delete(bst, value)
    elif choice == "3":
        value = int(input("Введите значение вершины для поиска: "))
        result = search(bst, value)
        if result is not None:
            print("Вершина найдена!")
        else:
            print("Вершина не найдена.")
    elif choice == "4":
        print("БДП:", end=' ')
        print_bst(bst)
        print()
    elif choice == "5":
        print("БДП:", end=' ')
        print_bst(bst)
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
