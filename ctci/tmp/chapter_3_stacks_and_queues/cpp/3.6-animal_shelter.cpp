#include <iostream>
#include <string>
#include <queue>

using namespace std;

class Animal
{
public:
    string name;

    Animal(){};
    Animal(string name);
    void setOrder(int order);
    bool isOlderThan(Animal other);

private:
    int order;
};

/**
 * Animal constructor.
 */
Animal::Animal(string name)
{
    this->name = name;
}

/**
 * Order setter.
 */
void Animal::setOrder(int order)
{
    this->order = order;
}

/**
 * Determines if this animal's order is earlier than another.
 */
bool Animal::isOlderThan(Animal other)
{
    return this->order < other.order;
}

class Dog : public Animal
{
public:
    Dog() : Animal(){};
    Dog(string name) : Animal(name){};
};

class Cat : public Animal
{
public:
    Cat() : Animal(){};
    Cat(string name) : Animal(name){};
};

class AnimalQueue
{
public:
    queue<Dog> dogs;
    queue<Cat> cats;

    AnimalQueue(){};
    void enqueueDog(Dog dog);
    void enqueueCat(Cat cat);
    Animal dequeueAny();
    Dog dequeueDog();
    Cat dequeueCat();

private:
    /* Order is used as a sort of timestamp, so that we can compare the
     * insertion order of a dog to a cat. */
    int order = 0;
};

/**
 * Add a dog to dog queue.
 */
void AnimalQueue::enqueueDog(Dog dog)
{
    dog.setOrder(this->order);
    this->order++;
    this->dogs.push(dog);
}

/**
 * Add a cat to cat queue.
 */
void AnimalQueue::enqueueCat(Cat cat)
{
    cat.setOrder(this->order);
    this->order++;
    this->cats.push(cat);
}

/**
 * Look at tops of dog and cat queues, and pops the queue with the
 * oldest value.
 */
Animal AnimalQueue::dequeueAny()
{
    if (this->dogs.empty())
        return this->dequeueCat();
    else if (this->cats.empty())
        return this->dequeueDog();
    Cat c = this->cats.front();
    Dog d = this->dogs.front();
    if (c.isOlderThan(d))
        return this->dequeueCat();
    else
        return this->dequeueDog();
}

/**
 * Pops the oldest dog from dog queue.
 */
Dog AnimalQueue::dequeueDog()
{
    if (this->dogs.empty())
        throw runtime_error("empty queue");
    Dog d = this->dogs.front();
    this->dogs.pop();
    cout << "dequeing " << d.name << "!\n";
    return d;
}

/**
 * Pops the oldest cat from cat queue.
 */
Cat AnimalQueue::dequeueCat()
{
    if (this->cats.empty())
        throw runtime_error("empty queue");
    Cat c = this->cats.front();
    this->cats.pop();
    cout << "dequeing " << c.name << "!\n";
    return c;
}

int main()
{
    AnimalQueue aq;

    aq.enqueueDog(Dog("spot"));
    aq.enqueueDog(Dog("matador"));
    aq.enqueueCat(Cat("garfield"));
    aq.enqueueCat(Cat("grumpy"));
    aq.enqueueCat(Cat("smokey"));
    aq.dequeueCat(); // dequeing garfield!
    aq.dequeueDog(); // dequeing spot!
    aq.dequeueAny(); // dequeing matador!
    aq.dequeueAny(); // dequeing grumpy!

    return 0;
}