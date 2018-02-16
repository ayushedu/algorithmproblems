class QueueNode:
    
    def __init__(self, data):

        self.data = data
        self.next = None

class MyQueue:

    def __init__(self):

        self.first = None
        self.last = None

    def add(self, item):
        """Add item to end of queue"""

        t = QueueNode(item)

        if self.last not None:
            self.last.next = t

        self.last = t

        if self.first is None:
            self.first = self.last

    def remove(self):
        """Remove and return element from front"""

        if self.first is None:
            raise ValueError("Queue is empty.")
        
        data = self.first.data
        self.first = self.first.next
        
        if self.first is None:
            self.last = None

        return data

    def peek(self):
        """Return element from front"""

        if self.first is None:
            raise ValueError("Queue is empty")

        return self.first.data

    def isEmpty(self):
        return self.first is None
        
        
        
