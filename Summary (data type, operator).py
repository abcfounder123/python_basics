"""
"Summary"

1. Data Types
2. Operators

################################################

1. built-in data types ( 15, 19 )

1. str
2. int
3. float
4. complex
5. list
6. tuple
7. range
8. dict
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memory view
15. NoneType 

################################################

Callable Types

1. functions
2. methods
3. classes
4. lambda

################################################

2. name, definition & usage of built-in data types

################################################

3. names of notations

1. quote                --->   ' ', " ", ''' ''', """ """
                               single quotes, double quotes, triple quotes

2. decimal notation     --->   .
   decimal fractions    --->   .3            <---   3 / 10
   
3. j, i                 --->   root -1

4. square brackets      --->   [ ]

5. round brackets       --->   ( )
                               brackets, parenthesis
                    
6. curley brackets      --->   { }
                               braces

################################################

4.Creating built-in data types with notation 

1. str                  --->   ' ', " ", ''' ''', """ """ 
2. int                  --->   notation is an integer value    -> 1, 2, 3
3. float                --->   .
4. complex              --->   j
5. list                 --->   [ ]
6. tuple                --->   ( )
7. range
8. dict                 --->   { }
9. set                  --->   { }
10. frozenset           
11. bool                --->   notation is boolean value       -> True, False
12. bytes               --->   b
13. bytearray
14. memory view
15. NoneType            --->   notation is NoneType value      -> None

################################################

notation ( 8 )
1, 3, 4, 5, 6, 8, 9, 11


################################################

value ( 3 )

2, 11, 15

################################################

no notation ( 4 )

7. range
10. frozenset  
13. bytearray
14. memory view

################################################
################################################

5. Creating built-in data types with name ( type casting )

1. str
2. int
3. float
4. complex
5. list
6. tuple
7. range
8. dict
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memoryview

################################################

15. NoneType            <---   only notation value None

################################################

6. checking data type with type function

################################################

7. Type Casting (explicit, implict(indirect))

float(1) + 1.6

1 + 1.6

################################################
################################################

operators ( 44 )
1. Operand
2. Binary Operator     --->   40
3. Unary operator      --->   4  (+, -, not, ~)       (U2, not 2)
4. Precedence          --->   15 (e, u, */, +-,  shift, and, or 2,  C, not, and, or,  t, assignment, walrus)
5. Associativity       --->   l 28, r 16 (exponent)(Assignment Operators 13)(Walrus)(lambda)(**, =)
6. Names of all operators

(1 + 2) - 3

2 ** (3 ** 3)
x = (y = 2)

################################################

U2, not 2
eawl
e, u, */, +-,  shift, and, or 2,  C, not, and, or,  t, assignment, walrus

################################################

1. Operand
   >> left operand
   >> right operand
   
     1    +    2
    /     |     \
  left    |     right
       operator
(addinional operation)  

################################################

2. Operator
   >> binary operator  --->   left + right, 1 + 2   
   
   >> unary operator   --->   right 
      1. unary plus    --->   + 1
      2. unary minus   --->   - 1
      3. logical NOT   --->   not True
      4. bitwise NOT   --->   ~ 5

################################################

3. Precedence
      
################################################

4. Associativity
   >> left sided bind
   >> right sided bind ( **, = ) (Assignment Operators 13)(Walrus)(lambda)

################################################

3. Precedence
>> parenthesis        --->   ( )
   
>> Arithmetic operator (Perform mathematical operations)( e, u, * /, + - )(9)
1. exponentiation     --->   **  
2. unary +, -         --->   +1, -1, ~
3. multiplication     --->   *
   division   
   division           --->   /
   floor division     --->   //
   modulus            --->   %
4. addition           --->   +
   substraction       --->   -

>> Bitwise Operators (Operate on bits)(shift, and, or2, not)(6)
5. Left shift         --->   <<
   Right shift        --->   >>

6. Bitwise AND        --->   &

7. Bitwise XOR        --->   ^

8. Bitwise OR         --->   |

2. Bitwise NOT        --->   ~

9. 
Comparison Operators (Compare values)(6)
   Equal to           --->   ==
   Not equal to       --->   !=
   Greater than       --->   >
   Less than          --->   <
   Greater than or equal to   --->   >=
   Less than or equal to      --->   <=

Identity Operators (Compare memory locations)
   Identical objects          --->   is
   Not identical objects      --->   is not

Membership Operators (Test for membership in sequences)
   Present in the sequence    --->   in
   Not present in the sequence --->   not in

>> Logical Operators (Combine conditional statements)
10.Logical NOT        --->   not
11.Logical AND        --->   and
12.Logical OR         --->   or
14.Assignment Operators (Assign values to variables) (13)
    Simple assignment --->   =
    Add and assign    --->   +=

################################################
################################################

Python operator precedence 
e, u, */, +-, 
shift, and, or 2, 
C, not, and, or, 
t, assignment, warlus

1. Exponentiation ** 
2. Unary Operators (+, -, ~) (Unary positive, negative, and logical NOT, bitwise NOT) 
3. Multiplication, Division, Modulus, Floor Division (*, /, %, //) 
4. Addition and Subtraction (+, -) 

5. Bitwise Shift Operators  (<<, >>) 
6. Bitwise AND (&) 
7. Bitwise XOR (^)
8. Bitwise OR (|) 

9. Comparison Operators (==, !=, >, <, >=, <=) 
   Identity Operators (is, is not) 
   Membership Operators (in, not in) 
10. Logical NOT (not) 
11. Logical AND (and) 
12. Logical OR (or)

13. conditional operator, ternary operator
14. Assignment Operators (13)
15. Special operator
    Walrus operator (assignment expression)(:= ( နောက်ဆုံးမှာရှိ )
      
    3. Matrix multiplication ( @ ) ( same as multiplication )

9 + 6 + 10 + 16 = 41 + 1 + 2  = 44

################################################

right sided bind (16) (**, =) 
1. **
2. Assignment Operators 13
4. Walrus Operator
5. lambda expression
    
################################################

1. Object ( RAM )
2. Memory address can be stored.
3. label, identifier, pointer
4. Label is a label. Object is an object.
5. Memory address can be overrided.
6. Dynamic type
7. Static type
8. Variable
9. There is no variable in Python.
10. 
variable   --->   data type
pointer    --->   memory address
identifier --->   all objects ( data, function, class, objects, module, ... )

11. Naming rules

################################################

Programming
>> Giving instructions to a computer
1. Instructions
2. Machine code
3. Executes

################################################

Three phases of a program
1. Input
2. Processing   <---
3. Output

################################################

Imperative Paradigm
1. Procedural Programming   <---
2. Object Oriented Programming

################################################

No "Best" Way, Only the "Right" Way

################################################

Procedural Programming
1. Sequences(top to buttom, left to right, parenthesis first)
2. Selection(if, else)    <---
3. Iteration(for, while)  <---
4. Functions

################################################
################################################

1.3.course overview

1. data type
-> built-in 15                                          <---
-> custom / user-defined data types
-> 10, 800 methods

################################################

2. control flow
-> operators ( 44 )
-> Loops and conditional statements ( while, if, for )   <---
-> practice (water motor, tac ti toe, calculator)

################################################

3. function
-> using built-in functions
-> rewriting built-in functions for better understanding
-> creating custom functions for specific tasks

################################################

4. OOP
-> objects & classes, relationships between objects ( inheritance, polymorphism, ... )
-> exercises
-> practice (chess game , django framework)

################################################

5. module
-> built-in modules
   -> about 300
   -> sys, math, os, datetime, pkgutil ( package + utilities for working with package )

-> external modules
   -> 400000 + ( Python package index ) ( PyPi )
   -> numpy, pandas, matplotlib, tensorflow, ...
   -> install, delete

################################################

6. error handling
-> syntax error
-> runtime error    <---   75
-> logical error
-> custom exception, error class

################################################

7. FP
-> programming paradigms ( imperative & declarative )
-> fundamentals concepts ( map, filter, iterator, recursion, .. )
-> control flow in FP ( functional methods to simplify loops(for) and conditions (if) )
-> exercises with FP concepts

################################################

8. Algorithm
-> basics of algorithm design and analysis
-> use cases in data structures
-> problem-solving & optimisation
-> algorithm -> about 1000, should know about 300
-> data structure algorithms --> about 100 ( 30 )

################################################

9. design patterns -> 23 ( all )

################################################
################################################
"""
