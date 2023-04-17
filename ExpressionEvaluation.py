import Construct_AST
import Evaluation


class ExpressionEvaluation:
    def __init__(self):
        pass

    def evaluate_expression(self, tokens):
        c_a = Construct_AST.Construct_AST()
        # print(tokens)
        ast = c_a.construct(tokens)
        # print(ast)
        # c_a.print_ast(ast)
        e = Evaluation.Evaluate()
        v = e.evaluate(ast)
        return v
