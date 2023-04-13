class Evaluate:
    def __init__(self):
        pass

    def operate(self, op2, op1, i):
        if i == '*':
            return float(op2) * float(op1)
        elif i == '/':
            return float(op2) / float(op1)
        elif i == '+':
            return float(op2) + float(op1)
        elif i == '-':
            return float(op2) - float(op1)
        elif i == '%':
            return float(op2) % float(op1)
        elif i == '^':
            return float(op2) ** float(op1)

    def evaluate(self, cur_node):
        type = cur_node.get('type', '')
        if type == 'Literal':
            return float(cur_node.get('value'))
        elif type == 'Binary':
            left = self.evaluate(cur_node.get('left'))
            right = self.evaluate(cur_node.get('right'))
            operator = cur_node.get('operator')
            return self.operate(left, right, operator)

