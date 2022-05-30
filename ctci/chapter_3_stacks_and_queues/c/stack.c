#include "stack.h"

/* Stack constructor */
node *new_node(int value)
{
    node *stack_node = malloc(sizeof(node));
    stack_node->value = value;
    stack_node->next = NULL;
    return stack_node;
}

/* Determines if a stack is empty */
int is_empty(node *root)
{
    return !root;
}

/* Pushes an element to the top of the stack */
void push(node **root, int value)
{
    node *stack_node = new_node(value);
    stack_node->next = *root;
    *root = stack_node;
}

/* Pops an element off the top of the stack */
int pop(node **root)
{
    node *temp;
    int popped;

    if (is_empty(*root))
    {
        printf("cannot pop...empty stack!\n");
        exit(1);
    }
    temp = *root;
    *root = temp->next;
    popped = temp->value;
    free(temp);

    return popped;
}

/* Peeks at the element at the top of the stack */
int peek(node *root)
{
    if (is_empty(root))
        return INT_MAX;
    return root->value;
}

/* Prints all elements of a stack */
void print_stack(node *root)
{
    while (root)
    {
        printf("%i ", root->value);
        root = root->next;
    }
    printf("\n");
}

/* Frees a stack */
void free_stack(node **root)
{
    node *current;
    node *tmp;

    if (!root)
        return;
    current = *root;
    while (current)
    {
        tmp = current;
        current = tmp->next;
        free(tmp);
    }
    *root = NULL;
    root = NULL;
}
