#include "tree.h"
#include "binary_search_tree.h"
#include "limits.h"

/**
 * Calculates differences between heights of left and right nodes.
 * If difference is greater than 1, return INT_MIN.
 */
int check_height(tree_node *root)
{
    int left_height, right_height, difference;

    if (!root)
        return -1;
    left_height = check_height(root->left);
    if (left_height == INT_MIN)
        return INT_MIN;
    right_height = check_height(root->right);
    if (right_height == INT_MIN)
        return INT_MIN;
    difference = left_height - right_height;
    if (abs(difference) > 1)
        return INT_MIN;
    return MAX(left_height, right_height) + 1;
}

/**
 * Determines if a binary tree is balanced. 
 */
int check_balanced(tree_node *root)
{
    return check_height(root) != INT_MIN;
}

int main(void)
{
    tree_node *root = NULL;
    tree_node *n5, *n15, *n12;
    int arr[] = {20, 10, 30, 5, 15};
    int size = sizeof(arr) / sizeof(int), i;

    for (i = 0; i < size; i++)
        insert(&root, arr[i]);
    printf("%i\n", check_balanced(root)); // 1
    insert(&root, 17);
    printf("%i\n", check_balanced(root)); // 0

    return 0;
}