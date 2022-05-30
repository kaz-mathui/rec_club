#include <iostream>
#include <limits>
#include <stack>

using namespace std;

class StackWithMin
{
public:
    stack<int> s1;
    /* New stack with minimums. */
    stack<int> s2;

    StackWithMin(){};
    void push(int value);
    int pop();
    int min();
};

/**
 * Pushes an element to the top of the stack.
 */
void StackWithMin::push(int value)
{
    if (value < this->min())
        s2.push(value);
    s1.push(value);
}

/**
 * Pops an element off the top of the stack.
 */
int StackWithMin::pop()
{
    int value = s1.top();
    if (value == this->min())
        /* If min is getting popped, remove from second list also. */
        s2.pop();
    s1.pop();
    return value;
}

/**
 * Return the minimum value of the stack.
 */
int StackWithMin::min()
{
    if (s2.empty())
        return INT32_MAX;
    return s2.top();
}

int main()
{
    StackWithMin swm;
    swm.push(1);
    swm.push(-5);
    swm.push(10);
    cout << swm.min() << endl; // -5
    swm.push(-10);
    cout << swm.min() << endl; // -10
    cout << swm.pop() << endl; // -10
    cout << swm.min() << endl; // -5

    return 0;
}