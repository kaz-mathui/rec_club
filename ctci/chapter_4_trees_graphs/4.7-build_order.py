from typing import List
Graph = __import__('graph').Graph


# TOPOLOGICAL SORT


class Project:
    def __init__(self, value: int):
        """
        Project constructor.
        """
        self.value = value
        self.map = set()
        self.dependencies = 0
        self.adjacent_list = []

    def add_adjacent(self, node: Project):
        """
        Adds an adjacent node.
        """
        if node.value not in self.map:
            self.adjacent_list.append(node)
            self.map.add(node.value)
            node.increase_dependencies()

    def increase_dependencies(self):
        """
        Increases dependencies by 1.
        """
        self.dependencies += 1

    def decrease_dependencies(self):
        """
        Decreases dependencies by 1.
        """
        self.dependencies -= 1

    def __str__(self) -> str:
        """
        String representation.
        """
        string = "Project = {\n" +\
                 f"\tvalue: {self.value}\n" +\
                 f"\tadjacents: {[a.value for a in self.adjacent_list]}\n" +\
                 f"\tmap: {[m.value for m in self.map]}\n" +\
                 f"\tdependencies: {self.dependencies}\n" +\
                 "}"
        return string


class Graph4_7(Graph):
    def __init__(self, directed: bool = True):
        """
        Graph constructor.
        """
        super().__init__()
        self.nodes_arr = []

    def add_vertex(self, value: int) -> Project:
        """
        Adds a new vertex to graph, or return existing one.
        """
        if value in self.nodes:
            return self.nodes[value]
        else:
            new_vertex = Project(value)
            self.nodes[value] = new_vertex
            self.nodes_arr.append(new_vertex)
            return new_vertex

    def __str__(self) -> str:
        """
        String representation.
        """
        string = "Graph = {\n" +\
                 f"\tdirected: {self.directed}\n" +\
                 f"\tnodes: {[k for k in self.nodes.values()]}\n" +\
                 f"\t: {[k for k in self.nodes_arr]}\n" +\
                 "}"
        return string


def find_build_order(dependencies: List[List[str]]) -> List[Project]:
    """
    Finds a correct build order.
    """
    graph = build_graph(dependencies)
    return order_projects(graph.nodes_arr)


def build_graph(dependencies: List[List[str]]) -> Graph4_7:
    """
    Builds the graph, adding the edge (a, b) if b is dependent on a. Assumes
    a pair is listed in "build order". The pair (a, b) in dependencies
    indicates that b depends on a and a must be built before b.
    """
    graph = Graph4_7()
    for pair in dependencies:
        first = pair[0]
        second = pair[1]
        graph.add_edge(first, second)
    return graph


def order_projects(projects: List[Project]) -> List[Project]:
    """
    Returns a list of the projects in a correct build order.
    """
    order = [None] * len(projects)
    to_be_processed = 0
    # Add roots to the build order first.
    end_of_list = add_non_dependent(order, projects, 0)
    while to_be_processed < len(order):
        curr = order[to_be_processed]
        # We have a circular dependency since there are no remaining
        # projects with zero dependencies.
        if not curr:
            return
        children = curr.adjacent_list
        for c in children:
            c.decrease_dependencies()
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
    return order


def add_non_dependent(order: List[Project], projects: List[Project], offset: int) -> int:
    """
    A helper function to insert projects with zero dependencies into the
    order array, starting at index offset.
    """
    for project in projects:
        if project.dependencies == 0:
            order[offset] = project
            offset += 1
    return offset


if __name__ == "main":
    dependencies = [
        ["a", "e"],
        ["b", "a"],
        ["c", "a"],
        ["f", "a"],
        ["f", "b"],
        ["f", "c"],
        ["d", "g"],
        ["b", "e"]
    ]
    print([p.value for p in find_build_order(dependencies)])
    # ['f', 'd', 'b', 'c', 'g', 'a', 'e']
