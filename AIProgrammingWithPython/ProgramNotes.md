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


### Truth Value Testing
If we use a non-boolean object as a condition in an if statement in place of the boolean expression, Python will check 
for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of an 
object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered False in Python:

- constants defined to be false: None and False 
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '"", (), [], {}, set(), range(0)

### Iterable
An iterable is an object that can return one of its elements at a time. This can include sequence types, such as strings, 
lists, and tuples, as well as non-sequence types, such as dictionaries and files.


### Dictionaries

- When you iterate through a dictionary using a for loop, doing it the normal way, like
for n in some_dict , will only give you access to the keys in the dictionary.
- For obtaining both key and value, use .items() method which generates a tuple of key value.

### Zip & Enumerate:
- zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements
in that position from all the iterables.
- enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.

### List comprehension:
- You create a list comprehension with brackets [], including an expression to evaluate for each element in an iterable.
- 