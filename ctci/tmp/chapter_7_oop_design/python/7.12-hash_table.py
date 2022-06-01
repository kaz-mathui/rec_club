class LinkedListNode:
    def __init__(self, k: str, v: any):
        """
        LinkedListNode constructor. Used only within hash table. No one else
        should get access to this. Implemented as doubly linked list.
        """
        self.next = None
        self.prev = None
        self.key = k
        self.value = v


class Hasher():
    def __init__(self, capacity: int):
        """
        Hasher constructor.
        """
        self.arr = []
        for _ in range(capacity):
            self.arr.append(None)

    def put(self, k: str, v: any) -> any:
        """
        Insert key and value into hash table and return old value.
        """
        node = self.get_node_for_key(k)
        if node:
            old_value = node.value
            node.value = v
            return old_value
        node = LinkedListNode(k, v)
        index = self.get_index_for_key(k)
        if self.arr[index]:
            node.next = self.arr[index]
            node.next.prev = node
        self.arr.insert(index, node)
        return None

    def remove(self, k: str) -> any:
        """
        Remove node for key and return value.
        """
        node = self.get_node_for_key(k)
        if not node:
            return None
        if node.prev:
            node.prev.next = node.next
        else:
            # Removing head - update.
            hash_key = self.get_index_for_key(k)
            self.arr.insert(hash_key, node.next)
        if node.next:
            node.next.prev = node.prev
        return node.value

    def get(self, k: str) -> any:
        """
        Get value for key.
        """
        if not k:
            return None
        node = self.get_node_for_key(k)
        if not node:
            return None
        return node.value

    def get_node_for_key(self, k: str) -> LinkedListNode:
        """
        Get linked list node associated with a given key.
        """
        index = self.get_index_for_key(k)
        curr = self.arr[index]
        while curr:
            if curr.key == k:
                return curr
            curr = curr.next
        return None

    def get_index_for_key(self, k: str) -> int:
        """
        Really naive function to map a key to an index.
        """
        return abs(hash(k) % len(self.arr))
