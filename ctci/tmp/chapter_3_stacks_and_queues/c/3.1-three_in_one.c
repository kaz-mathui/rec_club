#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct FixedMultiStack
{
    int num_of_stacks;
    int stack_capacity;
    int size;
    int *values;
    int sizes[3];
} fms;

/**
 * Fixed multi-stack constructor.
 */
fms *create_fixed_multi_stack(int stack_capacity)
{
    fms *stack;
    int i;

    stack = malloc(sizeof(fms));
    stack->num_of_stacks = 3;
    stack->stack_capacity = stack_capacity;
    stack->size = 3 * stack_capacity;
    stack->values = calloc(stack->size, sizeof(int));
    for (i = 0; i < stack->num_of_stacks; i++)
        stack->sizes[i] = 0;
    return stack;
}

/**
 * Prints all elements of a fixed multi-stack.
 */
void print_fms_values(fms *stack)
{
    int i;

    for (i = 0; i < stack->size; i++)
        printf("%i ", stack->values[i]);
    printf("\n");
}

/**
 * Prints all sizes of a fixed multi-stack.
 */
void print_fms_sizes(fms *stack)
{
    int i;

    for (i = 0; i < stack->num_of_stacks; i++)
        printf("%i ", stack->sizes[i]);
    printf("\n");
}

/**
 * Returns the top index of a given stack.
 */
int index_of_top(fms *stack, int stack_num)
{
    int offset, index;

    offset = stack->stack_capacity * stack_num;
    index = stack->sizes[stack_num];
    return offset + index - 1;
}

/**
 * Determines if a fixed multi-stack is full or not.
 */
int is_fms_full(fms *stack, int stack_num)
{
    return stack->sizes[stack_num] == stack->stack_capacity;
}

/**
 * Determines if a fixed multi-stack is empty or not.
 */
int is_fms_empty(fms *stack, int stack_num)
{
    return stack->sizes[stack_num] == 0;
}

/**
 * Pushes an element into a given stack.
 */
void push_fms(fms *stack, int stack_num, int value)
{
    int index;

    if (is_fms_full(stack, stack_num))
    {
        printf("stack is full!\n");
        return;
    }
    stack->sizes[stack_num]++;
    index = index_of_top(stack, stack_num);
    stack->values[index] = value;
    printf("pushing %i...\n", value);
}

/**
 * Pops the top element off a fixed multi-stack.
 */
int pop_fms(fms *stack, int stack_num)
{
    int index, temp;

    if (is_fms_empty(stack, stack_num))
    {
        printf("stack is empty!\n");
        return INT_MIN;
    }
    index = index_of_top(stack, stack_num);
    temp = stack->values[index];
    stack->values[index] = 0;
    stack->sizes[stack_num]--;
    printf("popping %i...\n", temp);
    return temp;
}

/**
 * Frees a fixed multi-stack.
 */
void free_fms(fms *stack)
{
    free(stack->values);
    free(stack);
}

int main()
{
    fms *stack = create_fixed_multi_stack(4);
    print_fms_values(stack);
    /* 0 0 0 0 0 0 0 0 0 0 0 0 */
    print_fms_sizes(stack);
    /* 0 0 0 */
    printf("%i\n", index_of_top(stack, 1)); // 3
    printf("%i\n", is_fms_full(stack, 1));  // 0
    printf("%i\n", is_fms_empty(stack, 1)); // 1
    push_fms(stack, 1, 24);                 // pushing 24...
    push_fms(stack, 1, 25);                 // pushing 25...
    push_fms(stack, 1, 26);                 // pushing 26...
    push_fms(stack, 1, 27);                 // pushing 27...
    push_fms(stack, 1, 28);                 // stack is full!
    push_fms(stack, 2, 35);                 // pushing 35...
    print_fms_values(stack);
    /* 0 0 0 0 24 25 26 27 35 0 0 0 */
    print_fms_sizes(stack);
    /* 0 4 1 */
    pop_fms(stack, 1); // popping 27...
    pop_fms(stack, 1); // popping 26...
    pop_fms(stack, 1); // popping 25...
    pop_fms(stack, 1); // popping 24...
    pop_fms(stack, 1); // stack is empty!
    print_fms_values(stack);
    /* 0 0 0 0 0 0 0 0 35 0 0 0 */
    print_fms_sizes(stack);
    /* 0 0 1 */
    free_fms(stack);

    return 0;
}