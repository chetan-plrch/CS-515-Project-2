import Tokenizer
import Printer

segment_1 = '''
x = 1
y = 0
print x, y
print x, (x / y
'''

segments = [segment_1]

for seg in segments:
    t = Tokenizer.Tokenizer(seg)
    prgm = t.text
    lines = prgm.split('\n')
    x = Printer.Printer()
    for line in lines:
        x.assigner(line)
    