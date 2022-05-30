#ifndef SINGLY_LINKED_LISTS_
#define SINGLY_LINKED_LISTS_

#include <iostream>
#include "tree.h"

class Node
{
public:
    TreeNode *value;
    Node *next;

    Node(TreeNode *value);
};

class LinkedList
{
public:
    Node *head;
    int length;
    LinkedList();

    Node *add_node(TreeNode *node);
    void print_list();
};

#endif