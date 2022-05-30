#include "tree.h"
#include "binary_search_tree.h"
#include "singly_linked_list.h"

/**
 * Creates a linked list out of every level in a binary tree.
 */
sll_node **create_level_linked_list(tree_node *root, int height)
{
    sll_node **arr = malloc(sizeof(sll_node *) * height);
    sll_node *head = NULL, *tmp;
    int i = 0;

    add_node_sll(&head, root);
    arr[i] = head;
    while (list_len(head))
    {
        i++;
        tmp = head;
        head = NULL;
        /* Loop through all nodes in parent. */
        while (tmp)
        {
            if (tmp->n->left)
                add_node_sll(&head, tmp->n->left);
            if (tmp->n->right)
                add_node_sll(&head, tmp->n->right);
            tmp = tmp->next;
        }
        arr[i] = head;
    }
    return arr;
}

int main(void)
{
    tree_node *root = NULL;
    sll_node **arr;
    int i, height;
    int bst[] = {20, 10, 30, 5, 15, 25, 40};
    int size = sizeof(bst) / sizeof(int);

    for (i = 0; i < size; i++)
        insert(&root, bst[i]);
    height = find_height(root);
    arr = create_level_linked_list(root, height);
    for (i = 0; i < height; i++)
        print_list(arr[i]);
    /* 
    20
    30 -> 10
    15 -> 5 -> 40 -> 25
    */
    return 0;
}