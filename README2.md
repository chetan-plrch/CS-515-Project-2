your name and Stevens login
the URL of your public GitHub repo
an estimate of how many hours you spent on the project
a description of how you tested your code
any bugs or issues you could not resolve
an example of a difficult issue or bug and how you resolved
a list of the four extensions you’ve chosen to implement

How we tested our code.

We have build scripts to test all the things that we would require us to test for any edge case or a logically 
1. Associativity and precedence
    a. Precedence ordering is from loosest to tightest:
        + and - operators, left associative
        *, / and % operators, left associative
        ^ operator, right associative
        unary - operator, nonassociative
        ++ and -- operators, nonassociative

```
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
3. Parsing testing - test_parse.py file (includes parse error cases)
```
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
# Expressions
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
# Expressions
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
    a. Visualization: The AST format presents the expression in a tree-like structure, making it easier to understand the hierarchy of the expression and how the operators and operands are related to each other. This visualization can help in identifying syntax errors and logical mistakes in the expression.
    b. Traceability: The AST format allows you to trace the flow of the expression and identify the specific node that is causing the error. This can be helpful when dealing with large and complex expressions.

    a. Visual of the below expressions:
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




