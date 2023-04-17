import Tokenizer
import Printer
import sys


t = Tokenizer.Tokenizer(sys.stdin.read())
prgm = t.text
lines = prgm.split('\n')

x = Printer.Printer()
for line in lines:
  x.assigner(line)






