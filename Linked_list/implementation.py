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
