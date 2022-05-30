#ifndef TREE_NODE_
#define TREE_NODE_

#include <stdio.h>
#include <stdlib.h>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

typedef struct tree_node
{
    int value;
    struct tree_node *left;
    struct tree_node *right;
    struct tree_node *parent;
} tree_node;

tree_node *create_node(int value);
tree_node *add_left(tree_node *root, int value);
tree_node *add_right(tree_node *root, int value);
int find_height(tree_node *root);
void pre_order_traversal(tree_node *root);

#endif