import Tokenizer
import Construct_AST
import Evaluation

t = Tokenizer.Tokenizer(open('expression.txt').read())
token_lines = t.char_without_type_tokenized_lines()
for tokens in token_lines:
    c_a = Construct_AST.Construct_AST()
    ast = c_a.construct(tokens)
    c_a.print_ast(ast)
    e = Evaluation.Evaluate()
    v = e.evaluate(ast)
    print(v)

