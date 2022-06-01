#include "tree.h"
#include <climits>

/**
 * Calculates differences between heights of left and right nodes.
 * If difference is greater than 1, return INT_MIN.
 */
int check_height(TreeNode *root)
{
    if (!root)
        return -1;
    int left_height = check_height(root->left);
    if (left_height == INT_MIN)
        return INT_MIN;
    int right_height = check_height(root->right);
    if (right_height == INT_MIN)
        return INT_MIN;
    int difference = left_height - right_height;
    if (abs(difference) > 1)
        return INT_MIN;
    return max(left_height, right_height) + 1;
}

/**
 * Determines if a binary tree is balanced.
 */
bool check_balanced(TreeNode *root)
{
    return check_height(root) != INT_MIN;
}

int main()
{
    TreeNode *t1 = new TreeNode(1);
    TreeNode *t2 = t1->add_left(2);
    TreeNode *t3 = t1->add_right(3);
    TreeNode *t4 = t2->add_left(4);
    TreeNode *t5 = t2->add_right(5);
    TreeNode *t6 = t3->add_left(6);
    TreeNode *t7 = t3->add_right(7);

    cout << check_balanced(t1) << endl; // 1

    TreeNode *t8 = t6->add_right(8);
    TreeNode *t9 = t8->add_right(9);

    cout << check_balanced(t1) << endl; // 0

    return 0;
}
