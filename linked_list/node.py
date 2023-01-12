class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class DoubleNode:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None
