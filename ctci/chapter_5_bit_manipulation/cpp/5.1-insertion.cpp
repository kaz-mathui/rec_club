#include "helper.cpp"

/**
 * Insert m into n at bits i through j.
 */
int insert_bits(int n, int m, int i, int j)
{
  /* Create a mask to clear bits i through j in n. For simplicity, we'll use
   * 16 bits for the example. */
  int all_ones = ~0;
  /* 1s before position j, then 0s. */
  int left = all_ones << (j + 1);
  /* 1s after position i. */
  int right = (1 << i) - 1;
  int mask = left | right;
  /* Clear bits j through i then put m in there. */
  int n_cleared = mask & n;
  int m_shifted = m << i;
  return n_cleared | m_shifted;
}

int main()
{
  int n = 0b1111111111111111;
  int m = 0b10101;
  bin(insert_bits(n, m, 2, 6));
  cout << "========\n";
  /* 1111111111010111 */

  n = 0b1000000000000000;
  m = 0b10101;
  bin(insert_bits(n, m, 2, 6));
  /* 1000000001010100 */
  return 0;
}