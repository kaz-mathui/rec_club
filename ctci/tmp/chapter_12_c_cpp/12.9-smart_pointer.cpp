#include <cstdlib>

template <class T>
class SmartPointer
{
    /* The smart pointer class needs pointers to both the object itself and to
     * the ref count. These must be pointers, rather than the actual object or
     * ref count value, since the goal of a smart pointer is that reference
     * count is tracked across multiple smart pointers to one object. */
public:
    SmartPointer(T *ptr)
    {
        /* We want to set the value of T *ref, and set the reference counter
         * to 1. */
        ref = ptr;
        ref_count = (unsigned *)malloc(sizeof(unsigned));
        *ref_count = 1;
    }

    SmartPointer(SmartPointer<T> &sptr)
    {
        /* This constructor creates a new smart pointer that points to an
         * existing object. We will need to first set ref and ref_count to
         * sptr's object and ref_count. Then, because we created a new
         * reference to ref, we need to increment ref_count. */
        ref = sptr.ref;
        ref_count = sptr.ref_count;
        ++(*ref_count);
    }

    /* Override the equal operator, so that when you set one smart pointer
     * equal to another, the old smart pointer has its reference count
     * decremented and the new smart pointer has its reference count
     * incremented. */
    SmartPointer<T> &operator=(SmartPointer<T> &sptr)
    {
        if (this == &sptr)
            return *this;
        /* If already assigned to an object, remove one reference. */
        if (*ref_count > 0)
            remove();

        ref = sptr.ref;
        ref_count = sptr.ref_count;
        ++(*ref_count);
        return *this;
    }

    ~SmartPointer()
    {
        remove(); // Remove one reference to object.
    }

    T getValue()
    {
        return *ref;
    }

protected:
    void remove()
    {
        --(*ref_count);
        if (*ref_count == 0)
        {
            delete ref;
            free(ref_count);
            ref = NULL;
            ref_count = NULL;
        }
    }

    T *ref;
    unsigned *ref_count;
};
