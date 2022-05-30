#include "tree.h"

/** 
 * Helper.
 */
TreeNode *create_minimal_bst_helper(int *arr, int start, int end)
{
    if (start > end)
        return nullptr;
    int mid = (start + end) / 2;
    TreeNode *t = new TreeNode(arr[mid]);
    t->left = create_minimal_bst_helper(arr, start, mid - 1);
    t->right = create_minimal_bst_helper(arr, mid + 1, end);
    return t;
}

/**
 * Creates a binary search tree with minimal height out of sorted array.
 */
TreeNode *create_minimal_bst(int *arr, int size)
{
    return create_minimal_bst_helper(arr, 0, size - 1);
}

int main()
{
    int arr[] = {1, 4, 6, 8, 9, 12, 19, 21};
    int size = sizeof(arr) / sizeof(int);
    TreeNode *t;

    t = create_minimal_bst(arr, size);
    pre_order_traversal(t);
    /*
            8
          /   \
        4       12
       / \     /  \
      1   6   9    19
                   /
                 21
    */
    return 0;
}
