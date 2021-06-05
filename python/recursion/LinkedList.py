class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add(self, value):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def get_head(self):
        return self.head

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
