class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def print_nodes_value(start_node):
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next

def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


def len_nodes(start_node):
    current_node = start_node
    len = 0
    while current_node:
        len+=1
        current_node = current_node.next
    return len


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

first_node = Node(names[0])
prev_node = first_node
for name in names[1:]:
    next_node = Node(name)
    prev_node.next = next_node
    prev_node = next_node

print_nodes_value(first_node)
print(len_nodes(first_node))
