"""

1. Operand
   >> left operand
   >> right operand
   
     1    +    2
    /     |     \
  left    |     right
       operator
(addinional operation) 

1 + 2 (binary plus)

+1 (unary plus)

add()
pos()

sub()
neg()

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
   >> parenthesis        --->   ( )
   
   >> Arithmetic operator ( e, u, * /, + - )
   1. exponentiation     --->   **  
   2. unary +, -         --->   +1, -1
   3. multiplication     --->   *
      division   
         division           --->   /
         floor division     --->   //  (ceiling)      ( 2.5  ---> 2, 3 )
         modulus            --->   %
   4. addition           --->   +
      substraction       --->   -

      
(1 + 2) * 3   
3 * 3
9

1 + (2 * 3)
1 * 6
7

################################################

4. Associativity
   >> left sided bind
   >> right sided bind ( **, = )
   
2 ** 3 ** 4
8 ** 4
4096

2 ** 3 ** 4
2 ** 81
2417851639229258349412352
   
x = y = 1

################################################


"""

