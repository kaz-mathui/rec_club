#ifndef BINARY_SEARCH_TREE_
#define BINARY_SEARCH_TREE_

#include "tree.h"

using namespace std;

class BinarySearchTree
{
public:
    TreeNode *root;

    BinarySearchTree();
    TreeNode *insert(int value);

private:
    int size;

    void add_node(TreeNode *node, TreeNode *new_node);
};

#endif