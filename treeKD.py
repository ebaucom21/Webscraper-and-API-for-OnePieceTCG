
# An implementation of a KD-Tree from a dictionary of dictionarys of parameters
class TreeKD:
    # A node in the KD-Tree
    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None    # Left subtree
            self.right = None   # Right subtree
    
    # The KD-Tree itself built from a dictionary of dictionaries
    # This will build the whole tree
    def __init__(self, dict):
        self.head = None     # The head of the tree
        self.dict = dict     # Dictionary of params for every object you will add
        # List of parameters to use for the KD-Tree
        self.params = list(list(dict.values())[0].keys()) if dict else []
        # Build the tree from the dictionary
        for key in list(dict.keys()):
            self.head = self.insert(dict[key])
        
    # Insert a point into the KD-Tree
    def insert(self, point):
        if self.head is None:
            return self.Node(point)
        else:
            return self.insertHelper(self.head, point, 0)
            
    # Helper function to insert a point into the KD-Tree
    def insertHelper(self, head, point, depth):
        if head is None:
            return self.Node(point)
        
        # Calculate current dimension (depth % k)
        cd = depth % len(self.params)
        
        # Compare the new point with the current node's point
        if point[self.params[cd]] < head.point[self.params[cd]]:
            head.left = self.insertHelper(head.left, point, depth + 1)
        else:
            head.right = self.insertHelper(head.right, point, depth + 1)
        
        return head

    # Function to search for a point in the KD-Tree
    def search(self, params):
        return self.searchHelper(self.head, params, 0)
    
    # Helper function to search for a point in the KD-Tree
    def searchHelper(self, head, params, depth):
        if head is None:
            return None
        
        # If the point matches the current node's point, return it
        headParams = dict[head.point]
        for i in range(len(self.params)):
            if headParams[self.params[i]] != params[self.params[i]] and self.params[i] != None:
                break
        else:
            return head.point
            
        
        # Calculate current dimension (depth % k)
        cd = depth % len(self.params)
        
        # If the current dimension is not specified, search both subtrees
        if params[cd] == None:
            temp1 = self.searchHelper(head.left, params, depth + 1)
            if temp1 is not None:
                return temp1
            return self.searchHelper(head.right, params, depth + 1)
        elif params[cd] < head.point[self.params[cd]]:
            return self.searchHelper(head.left, params, depth + 1)
        else:
            return self.searchHelper(head.right, params, depth + 1)
        
    # TODO: Implement a way to populate a list of points that match the search criteria
        
    