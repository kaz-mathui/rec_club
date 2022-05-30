from collections import deque
from typing import Dict


class Person:
    pass


class Machine:
    pass


class Server:
    def __init__(self):
        """
        Server constructor.
        """
        self.machines = {}
        self.person_to_machine_map = {}


class PathNode:
    def __init__(self, p: Person, prev):
        """
        PathNode constructor.
        """
        self.person = p
        self.prev_node = prev

    def collapse(self, starts_with_root: bool) -> deque:
        """
        Combines a path of PathNodes into a singly linked list.
        """
        path = deque()
        node = self
        while node:
            if starts_with_root:
                path.append(node.person)
            else:
                path.appendleft(node.person)
            node = node.prev_node
        return path


class BFSData:
    def __init__(self, root: Person):
        """
        BFSData constructor.
        """
        self.to_visit = deque()
        self.visited = {}
        self.source_path = PathNode(root, None)
        self.to_visit.append(self.source_path)
        self.visited[root.get("id")] = self.source_path

    def is_finished(self):
        """
        Determines if list of nodes to visit is finished.
        """
        return not len(self.to_visit)


def merge_paths(bfs1: BFSData, bfs2: BFSData, connection: int) -> deque:
    """
    Merge paths between two BFSData nodes.
    """
    end1 = bfs1.visited.get(connection)  # end1 -> source
    end2 = bfs2.visited.get(connection)  # end2 -> dest
    path_one = end1.collapse(False)
    path_two = end2.collapse(True)  # reverse
    path_two.popleft()
    path_one.extend(path_two)
    return path_one


def search_level(people: Dict, primary: BFSData, secondary: BFSData):
    """
    Search one level and return collision, if any.
    We only want to search one level at a time. Count how many nodes are
    currently in the primary level and only do that many nodes. We'll
    continue to add nodes to the end.
    """
    count = len(primary.to_visit)
    for _ in range(count):
        # Pull out first node.
        path_node = primary.to_visit.popleft()
        person_id = path_node.person.id
        # Check if it's already been visited.
        if person_id in secondary.visited:
            return path_node.person
        # Add friends to queue.
        person = path_node.person
        friends = person.friends
        for friend_id in friends:
            if friend_id not in primary.visited:
                friend = people[friend_id]
                next_ = PathNode(friend, path_node)
                primary.visited[friend_id] = next_
                primary.to_visit.append(next_)
    return None


def find_path_bi_bfs(people: Dict, source: int, dest: int):
    """
    Performs bi-direction bread-first search between two nodes.
    """
    source_data = BFSData(people.get(source))
    dest_data = BFSData(people.get(dest))
    while not source_data.is_finished() and not dest_data.is_finished():
        # Search out from source.
        collision = search_level(people, source_data, dest_data)
        if collision:
            return merge_paths(source_data, dest_data, collision["id"])
        # Search out from destination.
        collision = search_level(people, dest_data, source_data)
        if collision:
            return merge_paths(source_data, dest_data, collision["id"])
    return None


"""
A depth-first search would not work well because it would find a path, not the
shortest. It is inefficient because users might be only be one degree of separation,
but we can potentially search millions of nodes in their subtrees before
finding this relatively immediate connection.
A bidirectional bfs is generally faster than a traditional bfs. However, it
requires having access to both nodes.
BFS: O(k**q)
BiBFS: O(k**(q/2))

Optimization: Reduce machine jumps
- Instead of randomly jumping from one machine to another, batch jumps
together -- e.g., it five of my friends live on one machine, look them all up
at once.
Optimization: Smart division of people and machines
- People are much more likely to be friends with people who live in the same
country as they do. Rather than randomly dividing people across machines, try
to divide them by country, city, state, and so on. This reduces the amount of
jumps.
"""
