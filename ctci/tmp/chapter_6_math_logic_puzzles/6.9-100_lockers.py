"""
For which rounds is a door toggled (open or closed)
A door n is toggled for each factor of n, including itself and 1. That is a
door 15 is toggled on rounds 1, 3, 5, and 15
When would a door be left open?
A door is left open if the number of factors (x) is odd.
When would x be odd?
The value x is odd if n is a perfect square. Here's why: pair n's factors by
their complements.

1 2 3 4 5 6 7 8 9 10
____________________
1 1 1 1 1 1 1 1 1 1
  0   0   0   0   0
    0     1     0   
      1       1
        0         1
          0
            0
              0
                1
                  0 
"""
