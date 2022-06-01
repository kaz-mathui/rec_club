#include "tree.h"

/**
 * Helper.
 */
tree_node *create_minimal_bst_helper(int *arr, int start, int end)
{
    int mid;
    tree_node *new_node;

    if (start > end)
        return NULL;
    mid = (start + end) / 2;
    new_node = create_node(arr[mid]);
    new_node->left = create_minimal_bst_helper(arr, start, mid - 1);
    new_node->right = create_minimal_bst_helper(arr, mid + 1, end);
    return new_node;
}

/**
 * Creates a binary search tree with minimal height out of sorted array.
 */
tree_node *create_minimal_bst(int *arr, int size)
{
    return create_minimal_bst_helper(arr, 0, size - 1);
}

int main(void)
{
    tree_node *root;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(arr) / sizeof(int);

    root = create_minimal_bst(arr, size);
    pre_order_traversal(root);
    /* 5 2 1 3 4 7 6 8 9 */
    return 0;
}