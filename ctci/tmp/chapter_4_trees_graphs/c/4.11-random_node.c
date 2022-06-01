#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct tree_node
{
    int value;
    int size;
    struct tree_node *left;
    struct tree_node *right;
} tree_node;

/**
 * Tree Node constructor
 */
tree_node *create_node(int value)
{
    tree_node *new_node;

    new_node = malloc(sizeof(tree_node));
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->value = value;
    new_node->size = 1;
    return new_node;
}

/**
 * Inserts a node into correct place in Binary Search Tree.
 */
void insert_in_order(tree_node *root, int value)
{
    if (value < root->value)
    {
        if (!root->left)
            root->left = create_node(value);
        else
            insert_in_order(root->left, value);
    }
    else
    {
        if (!root->right)
            root->right = create_node(value);
        else
            insert_in_order(root->right, value);
    }
    root->size++;
}

/**
 * Retrieves a random node in Binary Search Tree. 
 */
tree_node *get_random_node(tree_node *root)
{
    int left_side, random;

    left_side = !root->left ? 0 : root->left->size;
    random = rand() % root->size;
    if (random < left_side)
        return get_random_node(root->left);
    else if (random == left_side)
        return root;
    else
        return get_random_node(root->right);
}

int main(void)
{
    int arr[] = {30, 10, 15, 5, 7, 3, 35};
    int size = sizeof(arr) / sizeof(int), i;
    tree_node *root = create_node(20);

    srand(time(NULL));
    for (i = 0; i < size; i++)
        insert_in_order(root, arr[i]);
    i = 10;
    while (i--)
        printf("%i ", get_random_node(root)->value);
    /* 20 3 7 5 20 3 35 20 10 30 */
    return 0;
}