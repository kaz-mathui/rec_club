#include "singly_linked_list.h"

/**
 * Prints all the elements of a singly linked list.
 */
size_t print_list(const sll_node *h)
{
    size_t count = 0;

    while (h)
    {
        if (h->next)
            printf("%i -> ", h->n->value);
        else
            printf("%i\n", h->n->value);
        h = h->next;
        count++;
    }
    return (count);
}

/**
 * Returns the number of elements in a singly linked list.
 */
size_t list_len(const sll_node *h)
{
    size_t count = 0;

    while (h)
    {
        h = h->next;
        count++;
    }
    return (count);
}

/**
 * Adds a new node to the head of a singly linked list.
 */
sll_node *add_node_sll(sll_node **head, tree_node *n)
{
    sll_node *new_node = (sll_node *)malloc(sizeof(sll_node));

    if (!head || !new_node)
        return (NULL);
    new_node->n = n;
    new_node->next = NULL;
    if (*head)
        new_node->next = *head;
    *head = new_node;
    return (new_node);
}
