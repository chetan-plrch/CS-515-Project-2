import Construct_AST
import Evaluation


class ExpressionEvaluation:
    def __init__(self):
        pass

    def evaluate_expression(self, tokens):
        c_a = Construct_AST.Construct_AST()
      
        ast = c_a.construct(tokens)
        # c_a.print_ast(ast)
        e = Evaluation.Evaluate()
        v = e.evaluate(ast)
        return v
