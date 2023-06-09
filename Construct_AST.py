import Errors

class Construct_AST:
    def construct(self, tokens):
        try:
            precedence = {
                '&&': (1, 'left'),
                '||': (1, 'left'),
                '<': (2, 'left'),
                '>': (2, 'left'),
                '==': (2, 'left'),
                '!=': (2, 'left'),
                '<=': (2, 'left'),
                '>=': (2, 'left'),
                '+': (3, 'left'),
                '-': (3, 'left'),
                '*': (4, 'left'),
                '/': (4, 'left'),
                '%': (4, 'left'),
                '^': (5, 'right')
            }

            ast_stack = []
            op_stack = []

            for i, token in enumerate(tokens):
                if token in precedence:
                    if (i+1) < len(tokens) and tokens[i+1] in precedence and tokens[i+1] != '+' and tokens[i+1] != '-':
                        raise Errors.ParseError('Two operators are beside each other')
                    curr_precedence, curr_associativity = precedence[token]
                    while op_stack and op_stack[-1] != '(' and (precedence[op_stack[-1]][0] > curr_precedence or
                                                                (precedence[op_stack[-1]][0] == curr_precedence and curr_associativity == 'left')):
                        operator = op_stack.pop()
                        right = ast_stack.pop()
                        left = ast_stack.pop()
                        ast_stack.append({
                            'type': 'Binary',
                            'operator': operator,
                            'left': left,
                            'right': right
                        })
                    op_stack.append(token)
                elif token == '(':
                    op_stack.append(token)
                elif token == ')':
                    while op_stack and op_stack[-1] != '(':
                        operator = op_stack.pop()
                        right = ast_stack.pop()
                        left = ast_stack.pop()
                        ast_stack.append({
                            'type': 'Binary',
                            'operator': operator,
                            'left': left,
                            'right': right
                        })
                    op_stack.pop()
                else:
                    ast_stack.append({
                        'type': 'Literal' if self.is_number(token) else 'Identifier',
                        'value': token
                    })

            while op_stack:
                operator = op_stack.pop()
                right = ast_stack.pop()
                left = ast_stack.pop()
                ast_stack.append({
                    'type': 'Binary',
                    'operator': operator,
                    'left': left,
                    'right': right
                })

            if len(ast_stack) != 1:
                raise Errors.ParseError('parse error')
        except:
            raise Errors.ParseError('parse error')
        return ast_stack[0]

    def print_ast(self, node, prefix='', is_left=True):
        if node.get('right'):
            self.print_ast(node['right'], prefix + ('│   ' if is_left else '    '), False)
        if 'value' in node:
            print(prefix + ('└── ' if is_left else '┌── ') + node['value'])
        else:
            print(prefix + ('└── ' if is_left else '┌── ') + node['operator'])
        if node.get('left'):
            self.print_ast(node['left'], prefix + ('    ' if is_left else '│   '), True)

    def is_number(self,value):
        try: 
            x=float(value)
            return True
        except:
            return False

