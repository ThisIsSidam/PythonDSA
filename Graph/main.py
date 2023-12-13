# Name : Anshu Kumar Singh
# Date : 14/12/23
# Title : Graph

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"'{vertex}': {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_verter in self.adj_list[vertex]:
                self.adj_list[other_verter].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
graph = Graph()

graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(3, 4)
graph.add_vertex(5)
graph.add_edge(3, 5)
graph.print_graph()

print("--")
graph.remove_vertex(3)
graph.print_graph()