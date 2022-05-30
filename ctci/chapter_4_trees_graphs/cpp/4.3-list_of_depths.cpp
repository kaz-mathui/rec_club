#include "tree.h"
#include "binary_search_tree.h"
#include "singly_linked_list.h"

/**
 * Creates a linked list out of every level in a binary tree.
 */
vector<LinkedList *> create_level_linked_list(TreeNode *root)
{
    vector<LinkedList *> res;

    LinkedList *curr = new LinkedList();
    curr->add_node(root);
    while (curr->length)
    {
        Node *tmp = curr->head;
        res.push_back(curr);
        LinkedList *next = new LinkedList();
        /* Loop through all nodes in parent. */
        while (tmp)
        {
            if (tmp->value->left)
                next->add_node(tmp->value->left);
            if (tmp->value->right)
                next->add_node(tmp->value->right);
            tmp = tmp->next;
        }
        curr = next;
    }
    return res;
}

int main()
{
    BinarySearchTree bst;
    vector<LinkedList *> v;
    int arr[] = {20, 10, 30, 5, 3, 7, 15, 17};
    int size = sizeof(arr) / sizeof(int), i;

    for (i = 0; i < size; i++)
        bst.insert(arr[i]);
    v = create_level_linked_list(bst.root);
    for (auto ptr : v)
        ptr->print_list();
    /*
    20
    30 -> 10
    15 -> 5
    7 -> 3 -> 17
    */
    return 0;
}
