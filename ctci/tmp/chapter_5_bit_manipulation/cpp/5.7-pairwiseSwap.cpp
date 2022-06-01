#include "helper.cpp"

/**
 * Swap odd and even bits with as few instructions as possible.
 */
int swap_odd_even_bits(int n)
{
    /* 0xaaaaaaaa = 10101010101010101010101010101010 */
    /* 0x55555555 = 01010101010101010101010101010101 */
    int swap_odds = (n & 0xaaaaaaaa) >> 1;
    int swap_evens = (n & 0x55555555) << 1;
    return swap_odds | swap_evens;
}

int main()
{
    bin(swap_odd_even_bits(0b11111111)); // 11111111
    bin(swap_odd_even_bits(0b10101010)); // 01010101
    bin(swap_odd_even_bits(0b11100011)); // 11010011

    return 0;
}