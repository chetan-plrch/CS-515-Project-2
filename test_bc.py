import Tokenizer
import Printer

segment_1 = '''
x = 1
y = ++x + y
z = x + y 
print z, x, ++x, x++, x
'''

segment_2 = '''
pi = 3.14159
r = 2
area = pi * r^2
print area
'''

segment_3 = '''
x  = 3
y  = 5
z  = 2 + x * y
z2 = (2 + x) * y
print x, y, z, z2
'''

segment_4 = '''
x = 1



print x
'''

segment_5 = '''
print 5 - 1 - 1 - 1
print ((5 - 1) - 1) - 1
print 2 ^ 2 ^ 2
'''

segment_6 = '''
x = 1
/* 
x = 2
y = 3
*/
y = 4
# print 0
print x, y
'''

segments = [segment_1, segment_2, segment_3, segment_4, segment_5, segment_6]

for seg in segments:
    t = Tokenizer.Tokenizer(seg)
    prgm = t.text
    lines = prgm.split('\n')

    x = Printer.Printer()
    for line in lines:
      x.assigner(line)






