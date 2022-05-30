#include <stdlib.h>

/**
 * Allocates memory such that the memory address returned is divisible
 * by a specific power of two.
 * For example, align_malloc(1000, 128) will return a memory address
 * that is multiple of 128 and points to memory of size 1000 bytes.
 */
void *aligned_malloc(size_t require_bytes, size_t alignment)
{
    void *p1; // Initial block.
    void *p2; // Aligned block inside initial block.
    int offset = alignment - 1 + sizeof(void *);
    if ((p1 = (void *)malloc(require_bytes + offset)) == NULL)
        return NULL;
    p2 = (void *)(((size_t)(p1) + offset) & ~(alignment - 1));
    ((void **)p2)[-1] = p1;
    return p2;
}

void aligned_free(void *p2)
{
    void *p1 = ((void **)p2)[-1];
    free(p1);
}