class StackNode:

    def __init__(self, data):

        self.data = data
        self.next = None

class MyStack:

    def __init__(self):

        self.top = None
        
    def pop(self):
        """Remove and return the top item"""

        if self.top is None:
            raise ValueError("Empty Stack")

        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        """Add item on top"""

        t = StackNode(item)
        t.next = self.top
        self.top = t

    def peek(self):
        """Return top data"""

        if self.top is None:
            raise ValueError("Empty Stack")
        
        return self.top.data

    def isEmpty(self):
        
        return self.top is None        
