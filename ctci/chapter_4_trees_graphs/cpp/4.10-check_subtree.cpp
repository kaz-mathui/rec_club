#include "tree.h"
#include <string>
#include <string.h>

/**
 * Create a string representation of binary with a pre-order traversal.
 * All null attributes are replaced with 'X'.
 */
string get_order_string(TreeNode *node)
{
    if (!node)
        return "X";
    return to_string(node->value) + get_order_string(node->left) + get_order_string(node->right);
}

/**
 * Determines if a tree contains another tree.
 */
bool contains_tree(TreeNode *first_root, TreeNode *second_root)
{
    string s1 = get_order_string(first_root);
    string s2 = get_order_string(second_root);
    return strstr(s1.c_str(), s2.c_str());
}

int main()
{
    TreeNode *t1 = new TreeNode(20);
    TreeNode *t2 = t1->add_left(10);
    TreeNode *t3 = t1->add_right(30);
    TreeNode *t4 = t2->add_left(5);
    TreeNode *t5 = t2->add_right(15);
    TreeNode *t6 = t3->add_left(25);
    TreeNode *t7 = t3->add_right(50);
    TreeNode *n1 = new TreeNode(10);
    TreeNode *n2 = n1->add_left(5);
    TreeNode *n3 = n1->add_right(15);

    cout << contains_tree(t1, n1) << endl; // 1
    n3 = n1->add_right(55);
    cout << contains_tree(t1, n1) << endl; // 0

    return 0;
}