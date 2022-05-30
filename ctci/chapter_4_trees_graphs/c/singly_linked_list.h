#ifndef SINGLY_LINKED_LIST
#define SINGLY_LINKED_LIST

#include <stdio.h>
#include <stdlib.h>
#include "tree.h"

/* Singly linked list node */
typedef struct sll_node
{
    tree_node *n;
    struct sll_node *next;
} sll_node;

size_t print_list(const sll_node *h);
size_t list_len(const sll_node *h);
sll_node *add_node_sll(sll_node **head, tree_node *n);

#endif