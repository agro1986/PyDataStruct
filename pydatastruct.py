class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @property
    def length(self):
        length = 0
        next_node = self.head
        while next_node is not None:
            length += 1
            next_node = next_node.next
        return length

    def add(self, data):
        new_node = LinkedListNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
