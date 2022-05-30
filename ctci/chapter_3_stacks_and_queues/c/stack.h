#ifndef STACK_
#define STACK_

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

/* first in, last out */
typedef struct stack_node
{
    int value;
    struct stack_node *next;
} node;

node *new_node(int value);
int is_empty(node *root);
void push(node **root, int value);
int pop(node **root);
int peek(node *root);
void print_stack(node *root);
void free_stack(node **root);

#endif