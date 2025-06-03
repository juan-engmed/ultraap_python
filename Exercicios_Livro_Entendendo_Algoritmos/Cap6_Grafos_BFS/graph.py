class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f'{vertex}:{edges}')
            
custom_graph = Graph()
custom_graph.add_vertex('A')

custom_graph.print_graph()
    