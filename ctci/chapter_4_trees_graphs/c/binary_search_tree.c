#include "binary_search_tree.h"

/**
 * Inserts a node onto another node.
 */
void add_node(tree_node *first, tree_node *second)
{
    /* Insert in left side. */
    if (first->value < second->value)
    {
        /* Insert in right side. */
        if (!first->right)
        {
            /* If right node does not exist, insert. */
            first->right = second;
            second->parent = first;
        }
        else
            /* Recurse. */
            add_node(first->right, second);
    }
    else
    {
        /* Insert in right side. */
        if (!first->left)
        {
            /* If left node does not exist, insert. */
            first->left = second;
            second->parent = first;
        }
        else
            /* Recurse. */
            add_node(first->left, second);
    }
}

/**
 * Inserts a node into a Binary Search Tree.
 */
tree_node *insert(tree_node **root, int value)
{
    tree_node *new_node;

    new_node = create_node(value);
    if (*root)
        add_node(*root, new_node);
    else
        *root = new_node;
    return new_node;
}