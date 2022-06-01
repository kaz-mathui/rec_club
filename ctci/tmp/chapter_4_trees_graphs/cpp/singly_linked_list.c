#include "singly_linked_list.h"

/**
 * Node constructor.
 */
Node::Node(TreeNode *value)
{
    this->value = value;
    this->next = NULL;
};

/**
 * Singly linked list constructor.
 */
LinkedList::LinkedList()
{
    this->head = NULL;
    this->length = 0;
}

/**
 * Adds a new node to the head of a singly linked list.
 */
Node *LinkedList::add_node(TreeNode *node)
{
    Node *new_node = new Node(node);
    if (!this->head)
        this->head = new_node;
    else
    {
        new_node->next = this->head;
        this->head = new_node;
    }
    this->length++;
    return new_node;
}

/**
 * Prints all elements of a singly linked list.
 */
void LinkedList::print_list()
{
    Node *curr = this->head;
    while (curr->next)
    {
        cout << curr->value->value << " -> ";
        curr = curr->next;
    }
    cout << curr->value->value << endl;
}
