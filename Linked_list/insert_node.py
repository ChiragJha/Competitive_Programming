"""
1. Create a linkedList
2. Ability to add nodes to the LinkedList
3. Ability to traverse the LinkedList
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while True:
                if current_node.next is None:
                    break
                current_node = current_node.next
            current_node.next = node

    def traverse_list(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            current_node = self.head
            while True:
                if current_node.next is None:
                    print(current_node.data)
                    break
                print(current_node.data, '--> ', end="")
                current_node = current_node.next

    def add_head_node(self, node):
        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            self.head = node
            new_head = self.head
            new_head.next = old_head

    def length(self):
        current_node = self.head
        count = 0
        while True:
            if current_node.next is None:
                count += 1
                break
            count += 1
            current_node = current_node.next
        return count

    def insert_node(self, node, position):
        if position > self.length() - 1:
            return ('out of bounds')
        else:
            current_node = self.head
            current_position = 0
            while True:
                if current_position + 1 == position:
                    next_node = current_node.next
                    current_node.next = node
                    current_node.next.next = next_node
                    break
                current_node = current_node.next
                current_position += 1


# Create Nodes
node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
# Initialise LinkedList
linked_list = LinkedList()
# Add nodes to the linked list
linked_list.add_node(node1)
linked_list.add_node(node2)
linked_list.add_node(node3)

# Traverse Linked List
linked_list.traverse_list()
new_head = Node("head")
# Add new head
linked_list.add_head_node(new_head)
linked_list.traverse_list()

# test out of bounds
print(linked_list.insert_node(Node("test"), 10))

# add new node in the middle
node4 = Node("inserted_node")
linked_list.insert_node(node4, 2)
linked_list.traverse_list()
print(1 is 2, 1 == 2)
