# First in, first out.
class Queue():
    def __init__(self):
        """
        Queue constructor.
        """
        self.queue = []
        self.length = 0

    def enqueue(self, value: int):
        """
        Adds an element to the front of a queue.
        """
        self.queue.append(value)
        self.length += 1

    def dequeue(self) -> int:
        """
        Pops an element off the front of a queue.
        """
        self.length -= 1
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peeks at the element at the front of the queue.
        """
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Determines if a queue is empty.
        """
        return self.length == 0


if __name__ == 'main':
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    print(q.queue)  # [0, 1, 2, 3, 4]
    print(q.dequeue())  # 0
    print(q.peek())  # 1
