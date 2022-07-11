Queue = __import__('queue').Queue


class Animal:
    def __init__(self, name: str):
        """
        Animal constructor.
        """
        self.name = name
        self._order = 0

    @property
    def order(self) -> int:
        """
        Order getter.
        """
        return self._order

    @order.setter
    def order(self, value: int):
        """
        Order setter.
        """
        self._order = value

    def is_older_than(self, animal: Cat or Dog) -> bool:
        """
        Determines if this animal's order is earlier than another.
        """
        return self.order < animal.order


class Cat(Animal):
    def __init__(self, name: str):
        """
        Cat constructor.
        """
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name: str):
        """
        Dog constructor.
        """
        super().__init__(name)


class AnimalQueue:
    def __init__(self):
        """
        Animal queue constructor.
        """
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0

    def enqueue(self, animal: Dog or Cat):
        """
        Add an animal to correct queue.
        Order is used as a sort of timestamp, so that we can compare the
        insertion order of a dog to a cat.
        """
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        elif isinstance(animal, Dog):
            self.dogs.enqueue(animal)

    def dequeue_any(self) -> Dog or Cat:
        """
        Look at tops of dog and cat queues, and pops the queue with the oldest
        value.
        """
        if self.cats.is_empty():
            return self.dequeue_dogs()
        if self.dogs.is_empty():
            return self.dequeue_cats
        cat = self.cats.peek()
        dog = self.dogs.peek()
        if cat.is_older_than(dog):
            return self.dequeue_cats()
        else:
            return self.dequeue_dogs()

    def dequeue_cats(self) -> Cat:
        """
        Pops the oldest cat from cat queue.
        """
        return self.cats.dequeue()

    def dequeue_dogs(self) -> Dog:
        """
        Pops the oldest dog from dog queue.
        """
        return self.dogs.dequeue()


if __name__ == "main":
    aq = AnimalQueue()
    spot = Dog('spot')
    smokey = Cat('smokey')
    grumpy = Cat('grumpy')
    matador = Dog('matador')
    garfield = Cat('garfield')
    aq.enqueue(spot)
    aq.enqueue(smokey)
    aq.enqueue(grumpy)
    aq.enqueue(matador)
    aq.enqueue(garfield)
    print([x.name for x in aq.cats.queue], [x.name for x in aq.dogs.queue])
    # ['smokey', 'grumpy', 'garfield'] ['spot', 'matador']
    print(aq.dequeue_any().name)  # spot
    print(aq.dequeue_cats().name)  # smokey
    print(aq.dequeue_any().name)  # grumpy
