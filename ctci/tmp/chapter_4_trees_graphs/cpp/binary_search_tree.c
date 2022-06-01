#include "binary_search_tree.h"

/**
 * Binary Search Tree constructor.
 */
BinarySearchTree::BinarySearchTree()
{
    this->root = nullptr;
    this->size = 0;
}

/**
 * Inserts a node into a Binary Search Tree.
 */
TreeNode *BinarySearchTree::insert(int value)
{
    TreeNode *n = new TreeNode(value);
    if (!this->root)
        this->root = n;
    else
        this->add_node(this->root, n);
    this->size++;
    return n;
}

/**
 * Inserts a node onto another node.
 */
void BinarySearchTree::add_node(TreeNode *node, TreeNode *new_node)
{
    if (node->value < new_node->value)
    {
        /* Insert in right side. */
        if (!node->right)
        {
            /* If right node does not exist, insert. */
            node->right = new_node;
            new_node->parent = node;
        }
        else
            /* Recurse. */
            this->add_node(node->right, new_node);
    }
    else
    {
        /* Insert in left side. */
        if (!node->left)
        {
            /* If left node does not exist, insert. */
            node->left = new_node;
            new_node->parent = node;
        }
        else
            /* Recurse. */
            this->add_node(node->left, new_node);
    }
}
