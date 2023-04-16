import Tokenizer
import Construct_AST
import Evaluation

file_txt = open('expression.txt').read()
t = Tokenizer.Tokenizer('5')
token_lines = t.char_without_type_tokenized_lines()
for tokens in token_lines:
    print(tokens)

# print(t.tokenize())
# tokens = t.char_with_type_tokenized_lines()
# for l in tokens:
#     print(l)

# token_lines = t.char_without_type_tokenized_lines()
# for tokens in token_lines:
#     c_a = Construct_AST.Construct_AST()
#     ast = c_a.construct(tokens)
#     c_a.print_ast(ast)
#     e = Evaluation.Evaluate()
#     v = e.evaluate(ast)
#     print(v)


