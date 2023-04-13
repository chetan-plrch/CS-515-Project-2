import os
import signal
import subprocess
import Tokenizer
import Construct_AST
import Evaluation

t = Tokenizer.Tokenizer(open('expression.txt').read())
tokens = t.clean_tokenize()
c_a = Construct_AST.Construct_AST()
ast = c_a.construct(tokens)

e = Evaluation.Evaluate()
v = e.evaluate(ast)
print(v)


# print('s')
# start a subprocess
# p = subprocess.Popen(["bc", "./expression.txt"], stdout=subprocess.PIPE)
# out, err = p.communicate()
# print('out:', out, err)

