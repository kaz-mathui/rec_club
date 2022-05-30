#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class SetOfStacks
{
public:
    int length = 0;

    SetOfStacks(int capacity);
    void push(int value);
    int pop();
    stack<int> *getLastStack();

private:
    int capacity;
    vector<stack<int>> stacks;
};

/**
 * Set of stacks constructor.
 */
SetOfStacks::SetOfStacks(int capacity)
{
    this->capacity = capacity;
}

/**
 * Pushes an element to the top of the stack.
 */
void SetOfStacks::push(int value)
{
    stack<int> *last = this->getLastStack();
    if (!last || last->size() >= this->capacity)
    {
        /* Create new stack. */
        stack<int> newStack;
        newStack.push(value);
        this->stacks.push_back(newStack);
        this->length++;
    }
    else
    {
        /* Add to last stack. */
        last->push(value);
    }
}

/**
 * Returns the last stack in set of stacks.
 */
stack<int> *SetOfStacks::getLastStack()
{
    if (this->length == 0)
        return nullptr;
    return &this->stacks.back();
}

/**
 * Pops an element off the top of the stack.
 */
int SetOfStacks::pop()
{
    stack<int> *last = this->getLastStack();
    if (!last)
        throw runtime_error("stacks are empty");
    int value = last->top();
    last->pop();
    if (last->empty())
    {
        /* If stack is empty, remove it from stacks. */
        this->stacks.pop_back();
        this->length--;
    }
    return value;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int i;

    SetOfStacks sos(3);
    for (auto i : arr)
        sos.push(i);
    cout << sos.length << endl; // 3
    i = 7;
    while (i--)
        sos.pop();
    /* sos.pop() exception */

    return 0;
}