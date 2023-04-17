import os
import signal
import subprocess
import Tokenizer
import Construct_AST
import Evaluation
import Printer


file1 = open('expression.txt', 'r')
Lines = file1.read()

t = Tokenizer.Tokenizer(Lines)
Lines=t.text


x=Printer.Printer()
for i in Lines.split("\n"):
    x.assigner(i)


# t = Tokenizer.Tokenizer(open('expression.txt').read())
# tokens = t.clean_tokenize()
# c_a = Construct_AST.Construct_AST()
# ast = c_a.construct(tokens)

# e = Evaluation.Evaluate()
# v = e.evaluate(ast)
# print(v)


# print('s')
# start a subprocess
# p = subprocess.Popen(["bc", "./expression.txt"], stdout=subprocess.PIPE)
# out, err = p.communicate()
# print('out:', out, err)

