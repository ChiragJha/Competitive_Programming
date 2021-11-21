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

    def pop(self):
        if self.head is None:
            raise Exception("No node to delete")
        else:
            if self.head.next is None:
                self.head = None
                return
            current_node = self.head
            while True:
                if current_node.next.next is None:
                    break
                current_node = current_node.next
            current_node.next = None


# Create Nodes
node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
# Initialise LinkedList
linked_list = LinkedList()
# Add nodes to the linked list
print("added nodes 1,2,3")
linked_list.add_node(node1)
linked_list.add_node(node2)
linked_list.add_node(node3)
# Traverse Linked List
linked_list.traverse_list()
new_head = Node("head")
# Add new head
print("added new head node")
linked_list.add_head_node(new_head)
linked_list.traverse_list()
# Delete last node
print("popping last node")
linked_list.pop()
linked_list.traverse_list()
