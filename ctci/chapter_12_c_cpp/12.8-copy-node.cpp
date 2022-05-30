#include <iostream>
#include <map>

using namespace std;

class Node
{
public:
    int value;
    Node *other;
    Node *random;
    Node() { value = 0; };
    Node(int value);
};

typedef map<Node *, Node *> NodeMap;

/**
 * Helper. 
 */
Node *copy_recursive(Node *cur, NodeMap &nodeMap)
{
    if (cur == nullptr)
        return nullptr;
    NodeMap::iterator i = nodeMap.find(cur);
    if (i != nodeMap.end())
    {
        // We've been here before, return the copy.
        return i->second;
    }
    Node *node = new Node;
    nodeMap[cur] = node; // Map current before traversing links.
    node->other = copy_recursive(cur->other, nodeMap);
    node->random = copy_recursive(cur->random, nodeMap);
    return node;
}

/**
 * Returns a complete copy of a Node class. 
 */
Node *copy_structure(Node *root)
{
    NodeMap nodeMap; // We will need an empty map.
    return copy_recursive(root, nodeMap);
}