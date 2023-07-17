# NOTES #

## Arithmetic operators ##

- Addition: +
- Subtraction: -
- Multiplication: *
- Division: /
- Mod (the remainder after dividing): %
- Exponentiation (note that ^ does not do this operation, as you might have seen in other languages):**
- Divides and rounds down to the nearest integer: //

---

## Bitwise Operators ##

[Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

The Operators:

x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.

---

### Extra Information ###

[BitArray](https://wiki.python.org/moin/BitArray)

[BitManipulation](https://wiki.python.org/moin/BitManipulation)
 

[ErrorsAndExceptions]( https://docs.python.org/3/tutorial/errors.html)
Difference between Errors and Exceptions.

``An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it``

[String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
: Above is a link to most commonly used string methods in python.

[More String Methods](https://docs.python.org/3/library/stdtypes.html#textseq)

