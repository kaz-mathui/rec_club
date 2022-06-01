#include "stack.h"

/* First in, first out. */
typedef struct queue
{
    node *oldest;
    node *newest;
} qq;

/**
 * Adds an element to the front of a queue.
 */
void enqueue(qq *q, int value)
{
    push(&q->newest, value);
}

/**
 * Shift all elements from oldest stack to newest stack.
 */
void shift_stacks(qq *q)
{
    if (is_empty(q->oldest))
        while (!is_empty(q->newest))
            push(&q->oldest, pop(&q->newest));
}

/**
 * Pops an element off the front of a queue.
 */
int dequeue(qq *q)
{
    shift_stacks(q);
    return pop(&q->oldest);
}

/**
 * Peeks at the element at the front of the queue.
 */
int peek_queue(qq *q)
{
    shift_stacks(q);
    return peek(q->oldest);
}

int main()
{
    int i;
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(int);
    qq *q = malloc(sizeof(qq));

    for (i = 0; i < size; i++)
        enqueue(q, arr[i]);
    print_stack(q->newest);        // 5 4 3 2 1
    printf("%i\n", dequeue(q));    // 1
    print_stack(q->oldest);        // 2 3 4 5
    printf("%i\n", peek_queue(q)); // 2
    free(q);

    return 0;
}