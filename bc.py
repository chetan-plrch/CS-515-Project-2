import Tokenizer
import Printer
import sys
import Errors


try:
  t = Tokenizer.Tokenizer(sys.stdin.read())
except Errors.ParseError:
  print('parse error')
  exit(0)

prgm = t.text
lines = prgm.split('\n')

x = Printer.Printer()
for line in lines:
  x.assigner(line)

