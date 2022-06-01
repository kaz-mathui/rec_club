#include "tree.h"
#include <unordered_map>

using namespace std;

/**
 * Prints a hash table with key, value pairs. 
 */
template <class T>
void print_hash_table(unordered_map<T, T> *ht)
{
    cout << "{\n";
    for (auto e : *ht)
    {
        cout << "  '" << e.first << "' : " << e.second << "\n";
    }
    cout << "}\n";
}

/**
 * Returns value at key or zero if it does not exist.
 */
int get_or_zero(unordered_map<int, int> *ht, int key)
{
    unordered_map<int, int>::iterator it;

    it = ht->find(key);
    return it != ht->end()
               ? it->second
               : 0;
}

/**
 * Modifies a key in a hash table.
 */
void modify_hash_table(unordered_map<int, int> *ht, int key, int delta)
{
    int new_count = get_or_zero(ht, key) + delta;
    if (!new_count)
        ht->erase(key);
    else
        ht->insert(make_pair(key, delta));
}

/**
 * Helper.
 */
int fpws_helper(TreeNode *node, int target_sum, int running_sum, unordered_map<int, int> *path_count)
{
    if (!node)
        return 0;
    /* Count paths with sum ending at the current node. */
    running_sum += node->value;
    int matching_sum = running_sum - target_sum;
    int total_paths = get_or_zero(path_count, matching_sum);
    /* If runningSum equals targetSum, then one additional path starts at root.
     * Add in this path. */
    if (running_sum == target_sum)
        total_paths++;
    /* Increment pathCount, recurse, then decrement pathCount */
    modify_hash_table(path_count, running_sum, 1); // Increment pathCount.
    total_paths += fpws_helper(node->left, target_sum, running_sum, path_count);
    total_paths += fpws_helper(node->right, target_sum, running_sum, path_count);
    modify_hash_table(path_count, running_sum, -1); // Decrement pathCount.
    return total_paths;
}

/* Returns the amount of paths in a binary tree that equal a target sum. */
int find_paths_with_sum(TreeNode *root, int target_sum)
{
    return fpws_helper(root, target_sum, 0, new unordered_map<int, int>);
}

int main()
{
    TreeNode *n1 = new TreeNode(10);
    TreeNode *n2 = new TreeNode(5);
    TreeNode *n3 = new TreeNode(-3);
    n1->left = n2;
    n1->right = n3;
    TreeNode *n4 = new TreeNode(3);
    TreeNode *n5 = new TreeNode(1);
    n2->left = n4;
    n2->right = n5;
    TreeNode *n7 = new TreeNode(11);
    n3->right = n7;
    TreeNode *n8 = new TreeNode(3);
    TreeNode *n9 = new TreeNode(-2);
    n4->left = n8;
    n4->right = n9;
    TreeNode *n11 = new TreeNode(2);
    n5->right = n11;

    cout << find_paths_with_sum(n1, 8) << endl; // 3

    return 0;
}