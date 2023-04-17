class Evaluate:
    def __init__(self):
        pass

    def operate(self, op2, op1, i):
        if i == '*':
            return op2 * op1
        elif i == '/':
            return op2 / op1
        elif i == '+':
            return op2 + op1
        elif i == '-':
            return op2 - op1
        elif i == '%':
            return op2 % op1
        elif i == '^':
            return op2 ** op1
        elif i == '&&':
            return int((op2 != 0) and (op1 != 0))
        elif i == '||':
            return int((op2 != 0) or (op1 != 0))
        elif i == '<':
            return int(float(op2) < float(op1))
        elif i == '>':
            return int(float(op2) > float(op1))
        elif i == '==':
            return int(float(op2) == float(op1))
        elif i == '!=':
            return int(float(op2) != float(op1))
        elif i == '<=':
            return int(float(op2) <= float(op1))
        elif i == '>=':
            return int(float(op2) >= float(op1))

    def evaluate(self, cur_node):
        type = cur_node.get('type', '')
        if type == 'Literal':
            # changed by sid to check if float is causing the problem
            if cur_node.get('value').isdigit():
                return int(cur_node.get('value'))
            else:
                return float(cur_node.get('value'))
        elif type == 'Binary':
            left = self.evaluate(cur_node.get('left'))
            right = self.evaluate(cur_node.get('right'))
            operator = cur_node.get('operator')
            return self.operate(left, right, operator)
        else:
            raise Exception('Unrecognized type during evaluation!')

