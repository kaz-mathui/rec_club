#include <iostream>

using namespace std;

/**
 * Prints the last 10 lines of a file.
 * Reads the whole file once, but only ten lines will be in memory at any
 * given point.
 */
void print_last_10_lines(char *file_name)
{
    const int K = 10;
    ifstream file(file_name);
    string L[K];
    int size = 0;

    // Read file line by line into circular array. peek() so an EOF
    // following a line ending is not considered a separate line.
    while (file.peek() != EOF)
    {
        getline(file, L[size % K]);
        size++;
    }

    // Compute start of circular array, and the size of it.
    int start = size > K ? (size & K) : 0;
    int count = min(K, size);
    // Print elements in the order they were read.
    for (int i = 0; i < count; i++)
        cout << L[(start + i) % K] << endl
}