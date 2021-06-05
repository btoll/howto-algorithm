class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def delete(self, value):
        if not self.head:
            return None

        current = self.head

        if current.value == value:
            self.head = current.next
            current.next = None
        else:
            prev = current
            head = current.next
            while current:
                if current.value == value:
                    prev.next = current.next
                    break
                prev = current
                current = current.next

    def get(self, value):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def print(self):
        if not self.head:
            return None

        current = self.head
        values = []
        while current:
            print(current.value)
            values.append(current.value)
            current = current.next
        return values

    def reverse(self):
        if not self.head:
            return None

        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev
