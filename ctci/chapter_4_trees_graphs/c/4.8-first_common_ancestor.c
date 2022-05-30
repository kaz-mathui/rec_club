#include "tree.h"

/* LINK TO PARENTS EXIST */

/**
 * Finds the depth from a node of a binary tree. 
 */
unsigned int find_depth(tree_node *node)
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
tree_node *move_up_by(tree_node *node, unsigned int delta)
{
    tree_node *curr;

    curr = node;
    while (delta && curr)
    {
        curr = curr->parent;
        delta--;
    }
    return curr;
}

/* Finds the first common ancestor of two nodes in a binary tree if there are
 * links to parents. */
tree_node *find_common_ancestor(tree_node *p, tree_node *q)
{
    int delta;
    tree_node *first, *second;

    delta = find_depth(p) - find_depth(q);
    first = delta > 0 ? p : q;
    second = delta > 0 ? q : p;
    first = move_up_by(first, abs(delta));
    while (first && second && first != second)
    {
        first = first->parent;
        second = second->parent;
    }
    return first && second ? first : NULL;
}

/* LINK TO PARENTS DOES NOT EXIST */

/**
 * Determines if a node has another node in subtree.
 */
int covers(tree_node *root, tree_node *node)
{
    if (!root)
        return 0;
    if (root == node)
        return 1;
    return covers(root->left, node) || covers(root->right, node);
}

/**
 * Helper.
 */
tree_node *common_ancestor_helper(tree_node *root, tree_node *p, tree_node *q)
{
    int is_p_left;
    int is_q_left;
    tree_node *child_side;

    if (!root || root == p || root == q)
        return root;
    is_p_left = covers(root->left, p);
    is_q_left = covers(root->left, q);
    if (is_p_left != is_q_left)
        return root;
    child_side = is_p_left ? root->left : root->right;
    return common_ancestor_helper(child_side, p, q);
}

/**
 * Finds the first common ancestor of two nodes in a binary tree if there
 * are no links to parents. */
tree_node *common_ancestor(tree_node *root, tree_node *p, tree_node *q)
{
    if (!covers(root, p) || !covers(root, q))
        return NULL;
    return common_ancestor_helper(root, p, q);
}

int main(void)
{
    tree_node *root = create_node(1);
    tree_node *n2 = add_left(root, 2);
    tree_node *n3 = add_right(root, 3);
    tree_node *n4 = add_left(n2, 4);
    tree_node *n5 = add_right(n2, 5);
    tree_node *n6 = add_left(n3, 6);
    tree_node *n7 = add_right(n3, 7);
    tree_node *n8 = add_left(n4, 8);
    tree_node *n9 = add_right(n4, 9);
    tree_node *n10 = add_left(n5, 10);
    tree_node *n11 = add_right(n5, 11);

    printf("%i\n", find_common_ancestor(n8, n11)->value);  // 2
    printf("%i\n", find_common_ancestor(n8, n7)->value);   // 1
    printf("%i\n", find_common_ancestor(n6, n7)->value);   // 3
    printf("%i\n", common_ancestor(root, n8, n11)->value); // 2
    printf("%i\n", common_ancestor(root, n8, n7)->value);  // 1
    printf("%i\n", common_ancestor(root, n6, n7)->value);  // 3

    return 0;
}