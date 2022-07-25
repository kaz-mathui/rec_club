from typing import List


class GraphNode:
    def __init__(self, value: int):
        """
        Node constructor.
        """
        self.value = value
        self.adjacent_list = []

    def add_adjacent(self, node: GraphNode):
        """
        Adds an adjacent node.
        """
        self.adjacent_list.append(node)

    def remove_adjacent(self, node: GraphNode):
        """
        Removes an adjacent node.
        """
        self.adjacent_list.remove(node)

    def __str__(self) -> str:
        """
        String representation.
        """
        string = "GraphNode = {\n" +\
                 f"\tvalue: {self.value}\n" +\
                 f"\tadjacents: {[node.value for node in self.adjacent_list]}\n" +\
                 "}"
        return string


class Graph:
    def __init__(self, directed: bool = True):
        """
        Graph constructor.
        """
        self.nodes = {}
        self.directed = directed

    def add_vertex(self, value: int) -> GraphNode:
        """
        Adds a new vertex to graph, or return existing one.
        """
        if value in self.nodes:
            return self.nodes[value]
        else:
            new_vertex = GraphNode(value)
            self.nodes[value] = new_vertex
            return new_vertex

    def remove_vertex(self, value: int) -> GraphNode:
        """
        Removes vertex from graph.
        """
        vertex = self.nodes[value]
        if vertex:
            for v in self.nodes.values():
                # Removes edges connected to vertex.
                if vertex in v.adjacent_list:
                    v.remove_adjacent(vertex)
        del self.nodes[value]
        return vertex

    def add_edge(self, source: GraphNode, dest: GraphNode) -> List[GraphNode]:
        """
        Adds an edge between two vertexes.
        """
        source_node = self.add_vertex(source)
        dest_node = self.add_vertex(dest)
        source_node.add_adjacent(dest_node)
        # Bi-directional graphs.
        if not self.directed:
            dest_node.add_adjacent(source_node)
        return [source_node, dest_node]

    def remove_edge(self, source: GraphNode, dest: GraphNode) -> List[GraphNode]:
        """
        Removes an edge between two vertexes.
        """
        source_node = self.nodes[source]
        dest_node = self.nodes[dest]
        if source_node and dest_node:
            source_node.remove_adjacent(dest)
        if not self.directed:
            dest_node.remove_adjacent(source)
        return [source_node, dest_node]

    def __str__(self) -> str:
        """
        String representation.
        """
        string = "Graph = {\n" +\
                 f"\tdirected: {self.directed}\n" +\
                 f"\tnodes: {[k.value for k in self.nodes.values()]}\n" +\
                 "}"
        return string


if __name__ == "main":
    g = Graph()
    g.add_edge('sf', 'oakland')
    g.add_edge('sf', 'san bruno')
    g.add_edge('oakland', 'san leandro')
    print(g)
    # Graph = {directed: True, nodes: ['sf', 'oakland', 'san bruno', 'san leandro']}
    print(g.nodes['sf'])
    # GraphNode = {value: sf, adjacents: ['oakland', 'san bruno']}
    print(g.nodes['oakland'])
    # GraphNode = {value: oakland, adjacents: ['san leandro']}
    g.remove_vertex('oakland')
    print(g)
    # Graph = {directed: True, nodes: ['sf', 'san bruno', 'san leandro']}
    print(g.nodes['sf'])
    # GraphNode = {value: sf, adjacents: ['san bruno']}
