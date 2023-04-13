import Tokenizer
import Construct_AST
import Evaluation

t = Tokenizer.Tokenizer(open('expression.txt').read())
# print(t.tokenize())
tokens = t.tokenized_lines()
for l in tokens:
    print(l)

# c_a = Construct_AST.Construct_AST()
# ast = c_a.construct(tokens)

# e = Evaluation.Evaluate()
# v = e.evaluate(ast)
# print(v)
