#include "tree.h"

/**
 * Helper.
 */
bool validate_bst_helper(TreeNode *root, int *min, int *max)
{
    if (!root)
        return true;
    if ((min && root->value <= *min) || (max && root->value > *max))
        return false;
    if (!validate_bst_helper(root->left, min, &root->value) ||
        !validate_bst_helper(root->right, &root->value, max))
        return false;
    return true;
}

/**
 * Validates that a binary tree is a binary search tree.
 */
bool validate_bst(TreeNode *root)
{
    return validate_bst_helper(root, nullptr, nullptr);
}

int main()
{
    TreeNode *t1 = new TreeNode(20);
    TreeNode *t2 = t1->add_left(10);
    TreeNode *t3 = t1->add_right(30);
    TreeNode *t4 = t2->add_left(5);
    TreeNode *t5 = t2->add_right(15);
    TreeNode *t6 = t3->add_left(25);
    /* TreeNode *t7 = t3->add_right(27); 0 */
    TreeNode *t7 = t3->add_right(50);

    cout << validate_bst(t1) << endl; // 1

    return 0;
}
