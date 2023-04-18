# CS-515-Project-2

### Made by Chetan Jain and Siddharth Jain 

### cjain1, sjain70

## URL : https://github.com/chetan-plrch/CS-515-Project-2

## Estimated Man Hours : 80 hours ( combining both bandwidth ) 
We also worked in shifts in with majority of time in overlapping

## Testing 
Some non typicaly function were tested using doctest, then after a functionality was created then we created custom scripts which were used. 

you can run the scripts in the repo. 

We created a exhaustive list of expression and run on it, you find the exhaustive list in expression.txt 

we also created the following docs to test specefic functionalities.

You to check this name different files:

you can run :

In Linux : 
<code> python3 test_extras.py</code>

# How we tested our code.

We have build scripts to test all the cases that would be required to reach a logical conclusion for the correctness of our program

Test scripts that can be referred in the codebase are test_increment_decrement.py, test_relation.py, test_parse.py, test_extensions.py, test_bc.py, ops_extensions.py. All these scripts uses exhaustive list of expressions that we have run through our program and compare the value that our program generates with the value of what bc generates.

Below are the categories of concepts and expression types that we have tested by using listed expression, in several cases we have ran through couple of 100's of expressions by running a script and compared value with bc programmatically with a shell script

1. Associativity and precedence
    * Precedence ordering is from loosest to tightest:
    * \+ and - operators, left associative
    * *, / and % operators, left associative
    * ^ operator, right associative
    * unary - operator, nonassociative
    * ++ and -- operators, nonassociative
```
# We ran more than 200 expressions with different syntax, main subset of expressions is as follows:
  (5 - 3) * (2 + 6) / 4 ^ 2 % 3", 
  ((7 + 2) * 5) + x + 2 ^ 2 ^ 2"
  (12 / 3) - (3 + x) * (6 % 4) * 2"
  10 * (8 - 2) / (x + 3) ^ 2 % 2"
  ((6 + 4) / x) ^ (9 % 5) - (3 * 2)"
  8 + 6 / (4 * 2) - x % 3 ^ 2"
  (5 * 3) + (9 - 2) / 4 ^ x - 6 % 2"
  ((11 - 3) / 2) ^ (8 % 5) + (7 * 2) / 3"
  (6 + 2) * (8 / 4) ^ x % 5 - 1"
  (3 * 5) - ((7 + x) % 6) ^ 2 + 1 / 2"
  7 ^ (8 % x) * (5 - 3) + 1 / 2 - 4 * 3"
  (9 + 2) * 3 - (7 / 2) % 4 ^ 2"
  6 - (5 * x) / (4 + 1) ^ 2 % 3 ^ 2"
  ((8 / x) ^ 2) * (4 % 3) - (5 + 1)"
  (3 + 4) * (7 - 2) / 6 ^ 2 % 2"
  (6 * 5) - (x % 3) ^ 2 + (9 / 3)"
  (2 ^ 3) * (5 - 2) + 9 / (7 % 3) - 1"
  (3 - 1) ^ x + (8 / 2) % 4 * 2"
  5 + (6 * 3) - (x - 2) / 4 ^ 2"
  ((8 / 2) * 4) % 7 + 1 ^ 3"
  (5 * 2) - (10 % 3) ^ 2 / 4 + 1"
  (4 + 2) * (3 - 5) / 2 % 3 ^ 2"
```
2. Extension testing - op_extension.py file
```
These expressions cover most of op equals cases:
"a += (a < b) && (c >= d) && ((e != f) || (g == h))"
"a += (x != y) || (z >= w) && (p == q)"
"x *= (m >= n) || ((p != q) && (r < s))"
"q /= (a <= b) && (c > d) && (e > f) || (g != h) + 1"
"e %= (x > y) || (z == w) && (p < q)"
"x-=(a == b) || ((c != d) && (e <= f))"
"x^=(x >= y) && (z < w) || ((p != q) && (r > s))"
"e=(m != n) && (p >= q) || (r < s)"
"b-=   (a < b) || ((c == d) && (e >= f))"
"c-=(x <= y) && (z > w || p == q)"
```
3. Parsing testing - test_parse.py file (includes parse error cases)
```
# Cases theat we made to handle unique parse and divide by zero errors
Case 1:
Input:
x = 1
y = 0
print x, y
print x, x / y

Output:
1.0 0.0
1.0 divide by zero 


Case 2:
Input:
x = 1
y = 0
print x, y
print x, x / y
print 1

Output:
1.0 0.0
1.0 divide by zero

Case 3:
Input:
x = 1
y = 0
z = x / y
print x, y
print x, x / y
print 1

Output:
divide by zero

Case 4:
Input:
x = 1
y = 0
print x, y
print x, (x / y

Output:
1.0 0.0
parse error

Case 5:
Input:
x = 1
y = 0
print x, y
print x, (x / y
print 1

Output:
1.0 0.0
parse error

Case 6:
Input:
x = 1
y = 0
z = (x / y
print x, y
print x
print 1

Output:
parse error

Case 7:
Input:
x = 1
y = 0
z = x + (x / y * 6 - (5)
print x, y
print x
print 1

Output:
parse error

Case 8:
Input:
x = 1
y = 0
z = x + (x / y * 6 - (5)))
print x, y
print x
print 1

Output:
parse error

Case 8:
Input:
x = 1
y = 0
z = x + (x / y * 6 - (5)))
print x, y
print x
print 1

Output:
parse error

Case 9:
Input:
x = 1
y = 0
z = x + (x / y * * 6 6- 5)
print x, y
print x
print 1

Output:
parse error


Case 10:
Input:
x = 1
y = 0
z = x + (x / y y * * - 5)
print x, y
print x
print 1

Output:
parse error

```
```
# Segments of programs that we tested for handling parse related issues:
segment_1 = '''
x = 1
y = 0
print x, y
print x, (x / y
'''

segment_2 = '''
x = 1
y = 0
print x, y
print x, (x / y
print 1
'''

segment_3 = '''
x = 1
y = 0
z = (x / y
print x, y
print x
print 1
'''

segment_4 = '''
x = 1
y = 0
z = x + (x / y * 6 - (5)
print x, y
print x
print 1
'''

segment_5 = '''
x = 1
y = 0
z = x + (x / y * 6 - (5)))
print x, y
print x
print 1
'''

segment_6 = '''
x = 1
y = 0
z = x + (x / y * 6 - (5)))
print x, y
print x
print 1
'''

segment_7 = '''
x = 1
y = 1
z = x + (x / y * * 6 - 5)
print x, y
print x
print 1
'''

segment_8 = '''
x = 1
y = 1
z = x + (x / y y * - 5)
print x, y
print x
print 1
'''

segment_9 = '''
a = 5-- - b
'''
```
4. Relation operators - test_relation.py
```
# Expressions that we found really useful to cover all the cases
    "(a < b) && (c >= d) && ((e != f) || (g == h))",  
    "(x != y) || (z >= w) && (p == q)",  
    "(m >= n) || ((p != q) && (r < s))",  
    "(a <= b) && (c > d) && (e > f) || (g != h)",  
    "(x > y) || (z == w) && (p < q)",
    "(a == b) || ((c != d) && (e <= f))",  
    "(x >= y) && (z < w) || ((p != q) && (r > s))",  
    "(m != n) && (p >= q) || (r < s)",  
    "(a < b) || ((c == d) && (e >= f))",  
    "(x <= y) && (z > w || p == q)"
```
5. Increment / Decrement operators - test_increment_decrement.py
```
# Expressions that we found useful to cover all cases
  "++a + b-- * c++ - d + ++e",
  "f-- * ++g - ++h * i-- + j",
  "--k + ++l * m-- + n * o--",
  "p-- * ++q * --r + s-- - ++t",
  "u + ++v - w-- * x++ * --y + z",
  "++aa * bb-- * cc + --dd - ee++ + ff",
  "++gg - hh-- * ii++ * jj - kk-- + ll",
  "--mm * ++nn + oo-- * pp + qq-- - ++rr",
  "ss * --tt + uu-- - vv++ * ++ww - xx",
  "++yy - zz-- * aaa * bbb-- - ccc + ++ddd",
  "eee-- + ++fff * --ggg * hhh - iii-- + jjj",
  "kkk * ++ll - mm * --nn + ooo-- - ++pp",
  "++qq * --rr * ss-- + ++tt - uu + vvv--",
  "www-- - ++xxx * yyy-- * ++zz - aaa * bbb++",
  "ccc + ++ddd * eee-- - fff-- * --ggg + ++hhh",
  "iii-- * ++jjj * --kkk + lll-- + ++mmm - nnn",
  "++ooo - ppp-- * qqq++ * --rrr - sss + ttt--",
  "uuu-- * ++vv - www-- * ++xxx + yyy - zzz++",
  "++aaa * bbb-- + --ccc * ddd-- - eee * ++fff",
  "ggg-- * ++hhh - iii-- + jjj-- * kk++ + ll * --mmm"
```
6. Comments - clean_comments function
```
# These segments of strings contains all possible formats of comments that 

segment_1 = '''
y = 1 /* comment-2 */ +5
y = 1 /* comment-3 */
y = 1 /* comment-4 
*/ a= 5
/*fhdkhkfhs*/
/*kfhdksfskdj
*/
  /*dfjkhsfjh
     */
'''

segment_2 = '''
y = 1 /* comment-2 */ +5
y = 1 /* comment-3 */
y = 1 /* comment-4 
*/ a= 5
/*fhdkhkfhs*/
/*kfhdksfskdj
*/
  /*dfjkhsfjh
     */
/*y = 0
z = x + (x / y * 6 - 5)
jhfkdshfdg
df;g
fdgjdfhghkjdfg
dfg dfgdfgdf /
'''
```
7. Printing an expression in an Abstract Syntax Tree (AST) format
We wrote a print print_ast (in Construct_AST class) that helps us visualize any complex expression, the advantages:
    * Visualization: The AST format presents the expression in a tree-like structure, making it easier to understand the hierarchy of the expression and how the operators and operands are related to each other. This visualization can help in identifying syntax errors and logical mistakes in the expression.
    * Traceability: The AST format allows you to trace the flow of the expression and identify the specific node that is causing the error. This can be helpful when dealing with large and complex expressions.
    * Debugging: The AST console prints made with print_ast method helped us debug fast by the method of tree visualization

##### Visual's that helped us debug quick:

```
# Expression 1
((7 + 2) * 5) + x + 2 ^ 2 ^ 2
│           ┌── 2
│       ┌── ^
│       │   └── 2
│   ┌── ^
│   │   └── 2
└── +
    │   ┌── 0
    └── +
        │   ┌── 5
        └── *
            │   ┌── 2
            └── +

# Expression 2
(12 / 3) - (3 + x) * (6 % 4) * 2
│       ┌── 2
│   ┌── *
│   │   │       ┌── 4
│   │   │   ┌── %
│   │   │   │   └── 6
│   │   └── *
│   │       │   ┌── 0
│   │       └── +
│   │           └── 3
└── -
    │   ┌── 3
    └── /
        └── 12

# Expression 3
((6 + 4) / x) ^ (9 % 5) - (3 * 2)
│       ┌── 2
│   ┌── *
│   │   └── 3
└── -
    │       ┌── 5
    │   ┌── %
    │   │   └── 9
    └── ^
        │   ┌── 0
        └── /
            │   ┌── 4
            └── +
                └── 6

# Expression 4
((11 - 3) / 2) ^ (8 % 5) + (7 * 2) / 3
│       ┌── 3
│   ┌── /
│   │   │   ┌── 2
│   │   └── *
│   │       └── 7
└── +
    │       ┌── 5
    │   ┌── %
    │   │   └── 8
    └── ^
        │   ┌── 2
        └── /
            │   ┌── 3
            └── -
                └── 11

# Expression 5
(x >= y) && (z < w) || ((p != q) && (r > s))
│           ┌── 0
│       ┌── >
│       │   └── 0
│   ┌── &&
│   │   │   ┌── 0
│   │   └── !=
│   │       └── 0
└── ||
    │       ┌── 0
    │   ┌── <
    │   │   └── 0
    └── &&
        │   ┌── 0
        └── >=
            └── 0
```

## Flow Logic

![python calculator drawio (1)](https://user-images.githubusercontent.com/22773916/232635331-b0f37285-410d-4cd0-bf60-c6f7bb21ff13.png)


## Extra Work 
We create a tree representation of AST in order to debug better
![tree](https://user-images.githubusercontent.com/22773916/232636046-85f3c09b-7dbc-465b-a5d9-c69d5e3662cb.png)



## Bug that we could not solve 
The binary not (boolean negation - ! - operator) is having some problems, and there was less time to solve this as a result, so we didn't meet the standard for it's evaluation. BUT rest of the code and all other functionality including extensions are working really well.
are working fine

## An example of a difficult issue or bug and how you resolved
1. We were initially confused with increment and decrement operators and evaluated severally expression manually and did big of reading to understand it completely
2. In that process, what we got to know that unary increment and decrement has the highest precedence.
3. The technique we used it is by pre-computing unary increment and decrement values and substituting them in the expression before computing ast and doing final evaluation
Eg:
```
Expression: ++a + b-- * c++ - d + ++e
Steps in evaluation:
1. After pre-computation: 1 + 0 * 0 - 0 + 1
2. AST is generated according to associativity and precedence
3. Evaluation is called on the ast generated on (1 + 0 * 0 - 0 + 1) and final result is computed
```

## Extensions that we have implmented
1. Comment
2. Op-equals
3. Relational Operations
4. Boolean operations


## Example of one of the extension:

### Comments:
##### These segments of strings contains all possible formats of comments 
```
INPUT:

segment_2 = '''
y = 1 /* Pichu */ +5
y = 1 /* Bulbasur */
y = 1 /* Doremon
*/ 
a= 5
print y
/* jo jeeta wahi sikandar */
/*mumbo jumbo
*/
  /* Kitresu
     */


OUTPUT:
1

INPUT: 
/*y = 0
z = x + (x / y * 6 - 5)
jhfkdshfdg
df;g
fdgjdfhghkjdfg
dfg dfgdfgdf / 
'''

OUTPUT 
parse error
```
