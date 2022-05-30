#include "tree.h"
#include "binary_search_tree.h"

/**
 * Helper.
 */
int validate_bst_helper(tree_node *node, int *min, int *max)
{
    if (!node)
        return 1;
    if ((min && node->value < *min) || (max && node->value > *max))
        return 0;
    if (!validate_bst_helper(node->left, min, &node->value) ||
        !validate_bst_helper(node->right, &node->value, max))
        return 0;
    return 1;
}

/**
 * Validates that a binary tree is a binary search tree. 
 */
int validate_bst(tree_node *root)
{
    return validate_bst_helper(root, NULL, NULL);
}

int main(void)
{
    tree_node *root = NULL;
    tree_node *n5, *n15, *n12;

    insert(&root, 20);
    insert(&root, 10);
    insert(&root, 30);
    n5 = insert(&root, 5);
    insert(&root, 3);
    insert(&root, 7);
    n15 = insert(&root, 15);
    insert(&root, 17);

    printf("%i\n", validate_bst(root)); // 1
    n12 = create_node(12);
    n15->right = n12;
    printf("%i\n", validate_bst(root)); // 0

    return 0;
}