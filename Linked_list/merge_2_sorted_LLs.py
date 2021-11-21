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

    def delete_node(self, position):
        if self.head is None:
            raise Exception("No nodes to delete")
        if position > self.length() - 1:
            raise Exception("No node found at position:{}".format(position))
        else:
            current_node = self.head
            current_position = 0
            while True:
                if current_position + 1 == position:
                    break
                current_position += 1
                current_node = current_node.next
            node_to_delete = current_node.next
            node_to_replace_deleted_node = node_to_delete.next
            current_node.next = node_to_replace_deleted_node


def merge_sorted_linked_lists(l1, l2):
    i = j = -1
    sorted_list = LinkedList()
    current_l1_node = l1.head
    current_l2_node = l2.head
    while True:
        if current_l1_node is None:
            sorted_list.add_node(current_l2_node)
            break
        elif current_l2_node is None:
            sorted_list.add_node(current_l1_node)
            break
        if current_l1_node.data < current_l2_node.data:
            next_node = current_l1_node.next
            current_l1_node.next = None
            sorted_list.add_node(current_l1_node)
            current_l1_node = next_node
        else:
            next_node = current_l2_node.next
            current_l2_node.next = None
            sorted_list.add_node(current_l2_node)
            current_l2_node = next_node
    return sorted_list


# Create Nodes
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(5)
# Initialise LinkedList
linked_list1 = LinkedList()
# Add nodes to the linked list
print("added nodes 1,2,3")
linked_list1.add_node(node1)
linked_list1.add_node(node2)
linked_list1.add_node(node3)
linked_list1.add_node(node4)
# Traverse Linked List
linked_list1.traverse_list()

# Create Nodes
node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
# Initialise LinkedList
linked_list2 = LinkedList()
# Add nodes to the linked list
print("added nodes 2,4,6")
linked_list2.add_node(node1)
linked_list2.add_node(node2)
linked_list2.add_node(node3)
# Traverse Linked List
linked_list2.traverse_list()

# Merge the 2 lists
sorted_list = merge_sorted_linked_lists(linked_list1, linked_list2)
sorted_list.traverse_list()
