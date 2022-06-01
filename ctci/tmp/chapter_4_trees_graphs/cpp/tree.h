#ifndef TREE_NODE_
#define TREE_NODE_

#include <iostream>

class TreeNode
{
public:
    int value;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode(int value);

    TreeNode *add_left(int value);
    TreeNode *add_right(int value);
};

#endif