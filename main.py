import Tokenizer
import Printer


while True:
    line = input()
    t = Tokenizer.Tokenizer(line)
    Lines = t.text

    x = Printer.Printer()
    x.assigner(Lines)

