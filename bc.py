import Tokenizer
import Printer


line = input()
t = Tokenizer.Tokenizer(line)
Lines = t.text

x = Printer.Printer()
x.assigner(Lines)

