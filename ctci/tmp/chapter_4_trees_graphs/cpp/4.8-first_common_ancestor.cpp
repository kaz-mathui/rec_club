#include "tree.h"

/* LINK TO PARENTS DOES NOT EXIST */

/**
 * Determines if a node has another node in subtree. 
 */
bool covers(TreeNode *root, TreeNode *node)
{
    if (!root)
        return false;
    if (root == node)
        return true;
    return covers(root->left, node) || covers(root->right, node);
}

/**
 * Helper.
 */
TreeNode *common_ancestor_helper(TreeNode *root, TreeNode *p, TreeNode *q)
{
    if (!root || root == p || root == q)
        return root;
    bool is_p_left = covers(root->left, p);
    bool is_q_left = covers(root->left, q);
    if (is_p_left != is_q_left)
        return root;
    TreeNode *child_side = is_p_left ? root->left : root->right;
    return common_ancestor_helper(child_side, p, q);
}

/**
 * Finds the first common ancestor of two nodes in a binary tree
 * if there are no links to parents.
 */
TreeNode *common_ancestor(TreeNode *root, TreeNode *p, TreeNode *q)
{
    if (!covers(root, p) || !covers(root, q))
        return nullptr;
    return common_ancestor_helper(root, p, q);
}

/* LINK TO PARENTS EXIST */

/**
 * Finds the depth from a node of a binary tree. 
 */
unsigned int find_depth(TreeNode *node)
{
    unsigned int depth = 0;

    while (node)
    {
        node = node->parent;
        depth++;
    }
    return depth;
}

/**
 * Moves a node up by a given number of nodes.
 */
TreeNode *move_up_by(TreeNode *node, unsigned int delta)
{
    TreeNode *curr = node;

    while (delta && curr)
    {
        curr = curr->parent;
        delta--;
    }
    return curr;
}

/**
 * Finds the first common ancestor of two nodes in a binary tree
 * if there are links to parents.
 */
TreeNode *find_common_ancestor(TreeNode *p, TreeNode *q)
{
    int delta = find_depth(p) - find_depth(q);
    TreeNode *first = delta > 0 ? p : q;
    TreeNode *second = delta > 0 ? q : p;
    first = move_up_by(first, abs(delta));
    while (first && second && first != second)
    {
        first = first->parent;
        second = second->parent;
    }
    return first && second ? first : nullptr;
}

int main()
{
    TreeNode *root = new TreeNode(1);
    TreeNode *n2 = root->add_left(2);
    TreeNode *n3 = root->add_right(3);
    TreeNode *n4 = n2->add_left(4);
    TreeNode *n5 = n2->add_right(5);
    TreeNode *n6 = n3->add_left(6);
    TreeNode *n7 = n3->add_right(7);
    TreeNode *n8 = n4->add_left(8);
    TreeNode *n9 = n4->add_right(9);
    TreeNode *n10 = n5->add_left(10);
    TreeNode *n11 = n5->add_right(11);

    TreeNode *n15 = new TreeNode(15);

    TreeNode *solution = find_common_ancestor(n8, n11);
    cout << solution->value << endl; // 2
    solution = find_common_ancestor(n8, n5);
    cout << solution->value << endl; // 2
    solution = find_common_ancestor(n8, n7);
    cout << solution->value << endl; // 1
    solution = find_common_ancestor(n8, n15);
    cout << solution << endl; // 0

    solution = common_ancestor(root, n8, n11);
    cout << solution->value << endl; // 2
    solution = common_ancestor(root, n8, n5);
    cout << solution->value << endl; // 2
    solution = common_ancestor(root, n8, n7);
    cout << solution->value << endl; // 1
    solution = common_ancestor(root, n8, n15);
    cout << solution << endl; // 0
}