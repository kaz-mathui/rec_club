Graph = __import__('graph').Graph
GraphNode = __import__('graph').GraphNode


def search(graph: Graph, start: GraphNode, end: GraphNode) -> bool:
    """
    Searches a graph to see if there is a route between two nodes.
    """
    if start == end:
        return True
    queue = [start]
    visited = {}
    visited[start.value] = True
    while len(queue):
        curr = queue.pop()
        if curr:
            for neighbor in curr.adjacent_list:
                if neighbor.value not in visited:
                    if neighbor == end:
                        return True
                    else:
                        queue.append(neighbor)
                visited[neighbor.value] = True
    return False


if __name__ == "main":
    g = Graph(False)
    sf = g.add_vertex('sf')
    hayward = g.add_vertex('hayward')
    sj = g.add_vertex('sj')
    g.add_edge('oakland', 'sf')
    g.add_edge('oakland', 'berkeley')
    g.add_edge('sf', 'san bruno')
    g.add_edge('oakland', 'san leandro')
    g.add_edge('san leandro', 'hayward')
    g.add_edge('san bruno', 'hayward')
    print(g)
    """
    Graph = {
        directed: False
        nodes: ['sf', 'hayward', 'sj', 'oakland', 'berkeley', 'san bruno', 'san leandro']
    }
    """
    print(search(g, sf, hayward))  # True
    print(search(g, sf, sj))  # False
    g.add_edge('sj', 'hayward')
    print(search(g, sf, sj))  # True
    g.remove_vertex('sj')
    print(search(g, sf, sj))  # False
