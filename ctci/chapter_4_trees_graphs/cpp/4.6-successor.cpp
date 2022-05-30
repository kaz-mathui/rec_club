#include "tree.h"
#include "binary_search_tree.h"

/**
 * Traverse to most left child node.
 */
TreeNode *left_most_child(TreeNode *node)
{
    TreeNode *curr = node;
    while (curr->left)
        curr = curr->left;
    return curr;
}

/**
 * Returns the next in-order successive node.
 */
TreeNode *next_successor(TreeNode *node)
{
    /* If node has right child, traverse down and left. */
    if (node->right)
        return left_most_child(node->right);
    TreeNode *child = node;
    TreeNode *parent = child->parent;
    /* Traverse up to first parent whose left child is not original node
     * or previous parent. */
    while (parent && parent->left != child)
    {
        child = parent;
        parent = parent->parent;
    }
    return parent;
}

int main()
{
    BinarySearchTree bst;
    TreeNode *bst5, *bst17;
    TreeNode *s1, *s2;

    bst.insert(20);
    bst.insert(10);
    bst.insert(30);
    bst5 = bst.insert(5);
    bst.insert(3);
    bst.insert(7);
    bst.insert(15);
    bst17 = bst.insert(17);

    s1 = next_successor(bst5);
    cout << s1->value << endl; // 7
    s2 = next_successor(bst17);
    cout << s2->value << endl; // 20

    return 0;
}
