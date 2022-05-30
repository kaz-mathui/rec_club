#include "tree.h"

/**
 * Tree Node constructor.
 */
TreeNode::TreeNode(int value)
{
    this->value = value;
    this->left = nullptr;
    this->right = nullptr;
    this->parent = nullptr;
};

/**
 * Adds a node to the left.
 */
TreeNode *TreeNode::add_left(int value)
{
    TreeNode *new_node = new TreeNode(value);
    new_node->parent = this;
    this->left = new_node;
    return new_node;
}

/**
 * Adds a node to the right.
 */
TreeNode *TreeNode::add_right(int value)
{
    TreeNode *new_node = new TreeNode(value);
    new_node->parent = this;
    this->right = new_node;
    return new_node;
}

/**
 * Prints current node before child nodes.
 */
void pre_order_traversal(TreeNode *root)
{
    if (!root)
        return;
    cout << root->value << endl;
    pre_order_traversal(root->left);
    pre_order_traversal(root->right);
}
