from typing import List, Tuple, Optional

class Node:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.outgoing: List[Tuple["Node", int]] = []
        self.incoming: List[Tuple["Node", int]] = []
        self.weight_out = 0
        self.weight_in = 0
        
    def coords(self) -> Tuple[float, float]:
        return (self.x, self.y)
    
    def __repr__(self):
        return f"N({self.x}, {self.y})"
    
    
class Separator:
    def __init__(self):
        self.points: List[Tuple[float, float]] = []
        self.edges: list[Tuple[Tuple[float, float], Tuple[float,float]]] = []
        
    def add_point(self, point: Tuple[float, float]):
        self.points.append(point)
        
    def add_edge(self, p1: Tuple[float, float], p2: Tuple[float, float]):
        self.edges.append((p1, p2))
            
class BSTNode:
    def __init__(self, segments: List, separator: Separator, parent: Optional["BSTNode"]):
        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None
        self.parent: Optional["BSTNode"] = parent
        
        self.segments = segments
        self.separator = separator