eps = 1e-24

class Node:
    global_id = 0
    
    def __init__(self, x, y):
        self.id = Node.global_id
        Node.global_id += 1
        self.x = x
        self.y = y
        
        self.polygons = []
        self.edges = []
        
    def __eq__(self, other):
        return self.id == other.id
    
    def __repr__(self):
        return f"N{self.id}: ({self.x}, {self.y})"
        
class Edge:
    global_id = 0
    
    def __init__(self, n1, n2):
        self.id = Edge.global_id
        Edge.global_id += 1
        self.n1 = n1
        self.n2 = n2
        
        self.lpol = None
        self.rpol = None
        
    def __eq__(self, other):
        return self.id == other.id
        
    def __repr__(self):
        return f"E{self.id}, ({self.n1.id}, {self.n2.id})"
        
        
class Polygon:
    global_id = 0
    
    def __init__(self):
        self.id = Polygon.global_id
        Polygon.global_id += 1
        
        self.nodes = []
        self.edges = []
        
    def __eq__(self, other):
        return self.id == other.id
        
    def __repr__(self):
        return f"P{self.id}"
        