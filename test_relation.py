import Tokenizer
import Printer

lister = [
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
]

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

segments = [segment_1]

for seg in segments:
    print(seg)
    t = Tokenizer.Tokenizer(seg)
    prgm = t.text
    print(t.text)
    # lines = prgm.split('\n')
    # for line in lister:
    #     x = Printer.Printer()
    #     x.assigner('p='+line)
    #     x.assigner('print p')

    # x = Printer.Printer()
    # x.assigner('p=(x <= y) && (z > w || p == q)')
    # x.assigner('print p')
    