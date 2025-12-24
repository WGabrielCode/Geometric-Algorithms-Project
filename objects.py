eps = 1e-24

class Point:
    global_id = 0
    
    def __init__(self, x, y):
        self.id = Point.global_id
        Point.global_id += 1
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
    
    def __init__(self, p1, p2):
        self.id = Edge.global_id
        Edge.global_id += 1
        self.p1 = p1
        self.p2 = p2
        
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
        
        self.points = []
        self.edges = []
        
    def __eq__(self, other):
        return self.id == other.id
        
    def __repr__(self):
        return f"P{self.id}"
        