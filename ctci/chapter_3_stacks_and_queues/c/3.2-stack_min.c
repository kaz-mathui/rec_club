#include "stack.h"

typedef struct stack_with_min
{
    node *values;
    node *mins;
} swm;

/**
 * Stack with minimum constructor.
 */
swm *create_swm()
{
    swm *stack = malloc(sizeof(swm));
    stack->values = NULL;
    /* new stack with minimums */
    stack->mins = NULL;
    return stack;
}

/**
 * Return the minimum value of the stack.
 */
int min_swm(swm *stack)
{
    return peek(stack->mins);
}

/**
 * Pushes an element to the top of the stack.
 */
void push_swm(swm *stack, int value)
{
    if (value < min_swm(stack))
        push(&stack->mins, value);
    push(&stack->values, value);
}

/**
 * Pops an element off the top of the stack.
 */
int pop_swm(swm *stack)
{
    int value;

    value = pop(&stack->values);
    if (value == min_swm(stack))
        /* If min is getting popped, remove from second list also. */
        pop(&stack->mins);
    return value;
}

int main()
{
    int i;
    int arr[] = {5, 1, -3, 9, -4};
    int size = sizeof(arr) / sizeof(int);
    swm *stack = create_swm();

    for (i = 0; i < size; i++)
        push_swm(stack, arr[i]);
    print_stack(stack->values);
    /* -4 9 -3 1 5 */
    print_stack(stack->mins);
    /* -4 -3 1 5 */
    printf("%i\n", min_swm(stack)); // -4
    printf("%i\n", pop_swm(stack)); // -4
    print_stack(stack->values);
    /* 9 -3 1 5 */
    print_stack(stack->mins);
    /* -3 1 5 */
    printf("%i\n", min_swm(stack)); // -3
    printf("%i\n", pop_swm(stack)); // 9
    print_stack(stack->values);
    /* -3 1 5 */
    print_stack(stack->mins);
    /* -3 1 5 */
    free_stack(stack->values);
    free_stack(stack->mins);
    free(stack);

    return 0;
}