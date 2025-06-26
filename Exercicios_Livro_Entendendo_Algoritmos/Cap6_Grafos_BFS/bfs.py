from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
            return True
        return False
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return False
        for other in self.graph:
            if vertex in self.graph[other]:
                self.graph[other].remove(vertex)
        del self.graph[vertex]
        return True
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f'{vertex}:{edges}')
            
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.graph[vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
            
custom_graph = Graph()
custom_graph.add_vertex('A')
custom_graph.add_vertex('B')
custom_graph.add_edge('A', 'B')

custom_graph.print_graph()
custom_graph.bfs('A')
    