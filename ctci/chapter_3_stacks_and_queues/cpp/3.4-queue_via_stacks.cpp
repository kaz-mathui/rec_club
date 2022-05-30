#include <iostream>
#include <stack>

using namespace std;

/* First in, first out. */
class MyQueue
{
public:
    stack<int> newest;
    stack<int> oldest;

    MyQueue(){};
    void enqueue(int value);
    void shiftStacks();
    int dequeue();
    int peek();
};

/**
 * Adds an element to the front of a queue.
 */
void MyQueue::enqueue(int value)
{
    this->newest.push(value);
}

/**
 * Shift all elements from oldest stack to newest stack.
 */
void MyQueue::shiftStacks()
{
    if (this->oldest.empty())
        while (!this->newest.empty())
        {
            this->oldest.push(this->newest.top());
            this->newest.pop();
        }
}

/**
 * Pops an element off the front of a queue.
 */
int MyQueue::dequeue()
{
    this->shiftStacks();
    int value = this->oldest.top();
    this->oldest.pop();
    return value;
}

/**
 * Peeks at the element at the front of the queue.
 */
int MyQueue::peek()
{
    this->shiftStacks();
    return this->oldest.top();
}

int main()
{
    MyQueue mq;
    int arr[] = {1, 2, 3, 4, 5};

    for (auto i : arr)
        mq.enqueue(i);
    cout << mq.dequeue() << endl; // 1
    cout << mq.peek() << endl;    // 2

    return 0;
}