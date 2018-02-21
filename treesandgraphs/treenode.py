class TreeNode:
    
    def __init__(self, name):
        
        self.name = name
        self.left = None
        self.right = None
        self.visited = False

    def __str__(self):
        return str(self.name)
