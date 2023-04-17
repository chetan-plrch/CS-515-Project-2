import Tokenizer
import Printer

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


segments = [segment_9]

for seg in segments:
    t = Tokenizer.Tokenizer(seg)
    prgm = t.text
    lines = prgm.split('\n')
    x = Printer.Printer()
    for line in lines:
        x.assigner(line)
    