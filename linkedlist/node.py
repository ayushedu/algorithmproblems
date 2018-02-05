class Node:
    """
    LinkedList implementation
    """
    def __init__(self, d):
        self.d = d
        self.next = None

    def add(self, d):
        self.addToTail(d)

    def addToTail(self, d):
        """
        Add element to tail of the list
        """
        head = self.next
        
        while(head and head.next):
            head = head.next

        if head == None:
            head = self
        head.next = Node(d)

    def getData(self):
        """
        Collect linkedlist values in a list and return
        """
        data = []
        head = self
        while(head):
            data.append(head.d)
            head = head.next
        return data
