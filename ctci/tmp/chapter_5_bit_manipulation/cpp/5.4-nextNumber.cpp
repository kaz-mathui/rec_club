#include "helper.cpp"

/**
 * Gets next biggest integer with same amount of 1s in binary representation.
 */
int get_next(int n)
{
    int c = n;
    for (int c0 = 0; !(c & 1) && c; c >>= 1, c0++)
        ;
    for (int c1 = 0; c & 1; c >>= 1, c1++)
        ;
    /* Position of rightmost non-trailing zero. */
    int p = c0 + c1;
    n |= (1 << p);            // Flip rightmost non-trailing zero.
    n &= ~((1 << p) - 1);     // Clear all bits to the right of p.
    n |= (1 << (c1 - 1)) - 1; // Insert (c1 - 1) ones on the right.
    return n;
}

/**
 * Get next smallest integer with same amount of 1s in binary representation.
 */
int get_prev(int n)
{
    int c = n;
    for (int c1 = 0; (c & 1); c >>= 1, c1++)
        ;
    if (!c)
        return -1;
    for (int c0 = 0; !(c & 1) && c; c >>= 1, c0++)
        ;
    /* Position of rightmost non-trailing one. */
    int p = c0 + c1;
    /* Clears from bit p onwards. */
    n &= (~0) << (p + 1);
    /* Sequence of (c1 + 1) ones. */
    n |= ((1 << (c1 + 1)) - 1) << (c0 - 1);
    return n;
}

int main()
{
    bin(get_next(0b11011001111100));
    /* 11011010001111 */
    bin(get_prev(0b10011110000011));
    /* 10011101110000 */
    return 0;
}