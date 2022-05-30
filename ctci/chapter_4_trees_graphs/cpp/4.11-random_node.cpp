#include <iostream>
#include <cstdlib>

using namespace std;

class TreeNode
{
public:
    int size;
    int value;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int value);
    void insert_in_order(int value);
    TreeNode *get_ith_index(int index);
};

/**
 * TreeNode constructor with size attribute.
 */
TreeNode::TreeNode(int value)
{
    this->left = nullptr;
    this->right = nullptr;
    this->size = 1;
    this->value = value;
}

/**
 * Inserts a node into correct place in Binary Search Tree.
 */
void TreeNode::insert_in_order(int value)
{
    if (value < this->value)
    {
        if (!this->left)
            this->left = new TreeNode(value);
        else
            this->left->insert_in_order(value);
    }
    else
    {
        if (!this->right)
            this->right = new TreeNode(value);
        else
            this->right->insert_in_order(value);
    }
    this->size++;
}

/**
 * Retrieves the node at guven index.
 */
TreeNode *TreeNode::get_ith_index(int index)
{
    int left_size;

    left_size = !this->left ? 0 : this->left->size;
    if (index < left_size)
        return this->left->get_ith_index(index);
    else if (index == left_size)
        return this;
    else
        return this->right->get_ith_index(index - (left_size + 1));
}

class BinarySearchTree
{
public:
    BinarySearchTree();
    void insert_in_order(int value);
    TreeNode *get_random_node();

private:
    TreeNode *root;
    int size;
};

/**
 * Binary Search Tree constructor.
 */
BinarySearchTree::BinarySearchTree()
{
    this->root = nullptr;
    this->size = 0;
}

/**
 * Inserts a node into correct place in Binary Search Tree.
 */
void BinarySearchTree::insert_in_order(int value)
{
    if (!this->root)
        this->root = new TreeNode(value);
    else
        this->root->insert_in_order(value);
    this->size++;
}

/**
 * Retrieves a random node in Binary Search Tree. 
 */
TreeNode *BinarySearchTree::get_random_node()
{
    int index = rand() % this->size;
    return this->root->get_ith_index(index);
}

int main()
{
    BinarySearchTree *bst;
    int arr[] = {20, 30, 10, 15, 35, 10, 5, 7, 3};
    int size = sizeof(arr) / sizeof(int), i;

    srand(time(NULL));
    bst = new BinarySearchTree();
    for (i = 0; i < size; i++)
        bst->insert_in_order(arr[i]);
    i = 10;
    while (i--)
        cout << bst->get_random_node()->value << " ";
    /* 5 30 7 35 20 35 7 7 5 10 */
    delete bst;
    return 0;
}