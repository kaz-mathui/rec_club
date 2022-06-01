/**
 * Prints the binary presentation of an integer.
 */
void bin(int n)
{
    int flag = 0;
    /* Size of an integer is assumed to be 32 bits. */
    for (int i = 31; i >= 0; i--)
    {
        int k = n >> i;
        if (k & 1)
        {
            printf("1");
            flag = 1;
        }
        else if (flag)
            printf("0");
    }
    printf("\n");
}