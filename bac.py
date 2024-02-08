"""



2.1

name                     >>       int, integer, integer literal
definition               >>       integer

usage                    >>       directly use
description              >>       mathematical operation



################################################



name                     >>      str, string, string literal
definition               >>      charactor string

usage                    >>      ' ',  " ", '''  ''', """  """
description              >>      47 methods (upper, lower), concatination ( + ), * ( n th times )


"""
x = "I go to school."
y = x.upper()
print(x)
print(y)
"""

################################################


2.2

name                     >>       variable, identifier, label
definition               >>       ကိုယ်စားပြုအမည်
                                  Identifier  ( for all ) ( function, class, method)
                                  variable ( for values )
usage                    >>       =
description              >>       Python has five rules for naming idenfiers.
                                  1. An identifiers must contain at least one character.
                                  2. The first character of an identifiers must be an alphabetic letter (upper or lower case) or the underscore.
                                  3. The remaining characters (if any) may be alphabetic characters (upper or lower case), the underscore,
                                  4. No other characters (including spaces) are permitted in identifiers.
                                  5. A reserved word cannot be used as an identifier.



################################################

2.3

name                     >>       assignment operator
definition               >>       assign right ( value ) to left ( identifier )
usage                    >>       =
description              >>       += , -=, *=, /=  မူလတန်ဖိုးကိုပဲ ထပ်ပေါင်းချင်ရင်သုံး


################################################

Note
1. keyword.kwlist
2. tuple assign

################################################





2.4

name                     >>       float, floating-point number
definition               >>       number with .
usage                    >>       .
description              >>       1. continuous values 17
                                  2. store by 1/10                   --> 0.1 = 1/10
                                  3. int and float are different data types.
                                     so, they can not make operation directly.
                                     ( before operation, py changed int to float )

                                  4. rounding adds or subtracts to produce closest value
                                         >> round(float)
                                            --> one argument value       --> int
                                            --> two                      --> float                       <----------
                                                ( second arg may be positive(r) or negative(l) )

                                         >> round(int)
                                            --> one argument value       --> int
                                            --> two                      --> int                         <----------
                                                ----> positive second arg      --> original value
                                                ----> negative                 --> round value

                                  5. truncation to drop fractional part
                                         >> int()


note

1. scientific notation for exponent ( e ) ( e1 = 10, e2 = 100 )      -->   1e-10, 1e10 ( right / left )
2. predefined data type ( not for py )
   16bit = 2**16 = 65536 ( 32768 to - 32767 )
3. sys.getsizeof()
4. sys.floatinfo()
   --> min , max
5. bin()

################################################

2.5

name                     >>       control codes, escapse charactors, special charactors
definition               >>
usage                    >>       \
description              >>

1 .                        --->       \
2 .                        --->       '
3 .                        --->       "

4 . bell                   --->       a
5 . back space             --->       b
6 . form feed              --->       f
7 . new line               --->       n
8 . carriage return        --->       r
9 . horizontal tab        --->       t
10 . vertical tab          --->       v

11. unicode name                   --->       N{}
12 . hexadecimal                   --->       x00
13 . hexadecimal value             --->       u0000
     of unicode  ( 16 bit)
14 . hexadecimal value             --->       U00000000
     of unicode  ( 32 bit)
15 . octal value                   --->       000

( 97 ( 141, 61))

################################################

2.6

name                     >>       input
definition               >>
usage                    >>       input()
description              >>       receive input data as str

note
1. int()
2. float()
3. print()
4. root2        --->      exp(1/2)
   root3        --->      exp(1/3)

################################################



2.7

name                     >>       print
definition               >>
usage                    >>       print()
description              >>       1. print str value
                                  2. unlimited input data with ,
                                  3. positional arguments,
                                  4. keywoed arguments      --->   by nane
                                     for print()            --->   end, sep, file, flush ( in time )

note
1. open()

################################################

2.8

name                     >>       string formatting
definition               >>
usage                    >>       format(), f
description              >>

1. format()  >>>   positional argument    --->       "{}  {}  {}".format("apple", "banana", "orange")
                                          --->       "{2}  {1}  {0}".format("apple", "banana", "orange")
                                          --->        index error

             >>>   keyword argument       --->       "{f1}  {f2}  {f3}".format(f1="apple", f2="banana", f3="orange")

2. f         >>>   keyword argument       --->       f"{f1}  {f2}  {f3}"

3. format methods  ( f, a, t )
   >>   :
   >>   fill charactor
   >>   <^> alignment
   >>   total charactor

################################################

2.9 

name                     >>       multiline string, preformatted string
definition               >>
usage                    >>       """   """    ,    '''   '''
description              >>       auto complete \n


################################################

















"""
