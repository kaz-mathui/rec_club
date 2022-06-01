#include "stack.h"

/**
 * Sorts a stack using a secondary stack as a buffer.
 * O(n**2) time complexity and O(n) space complexity.
 */
void sort_stack(node *stack)
{
    int temp;

    node *buffer = NULL;
    while (!is_empty(stack))
    {
        temp = pop(&stack);
        while (!is_empty(buffer) && peek(buffer) > temp)
            /* If peeked value in buffer is less than temp, place back in stack. */
            push(&stack, pop(&buffer));
        push(&buffer, temp);
    }
    /* Place everything in buffer back into stack. */
    while (!is_empty(buffer))
        push(&stack, pop(&buffer));
}

int main()
{
    int i;
    node *stack = NULL;

    int arr[] = {4, 5, 2, 8, 1, 9, 6, 7, 3, 0};
    int size = sizeof(arr) / sizeof(int);

    for (i = 0; i < size; i++)
        push(&stack, arr[i]);
    print_stack(stack); // 0 3 7 6 9 1 8 2 5 4
    sort_stack(stack);
    print_stack(stack); // 0 1 2 3 4 5 6 7 8 9

    return 0;
}