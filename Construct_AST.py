class Construct_AST:
    def construct(self, tokens):
        # Define operator precedence and associativity
        precedence = {
            # '<': (1, 'left'),
            # '>': (1, 'left'),
            # '==': (1, 'left'),
            # '!=': (1, 'left'),
            # '<=': (1, 'left'),
            # '>=': (1, 'left'),
            # '&&': (1, 'left'),
            # '||': (1, 'left'),
            '+': (2, 'left'),
            '-': (2, 'left'),
            '*': (3, 'left'),
            '/': (3, 'left'),
            '%': (3, 'left'),
            '^': (4, 'right')
        }

        # Initialize AST stack and operator stack
        ast_stack = []
        op_stack = []

        # Iterate through tokens
        for token in tokens:
            if token in precedence:
                # Pop operators from op_stack and build AST nodes until precedence and associativity is satisfied
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
                # Push current operator onto op_stack
                op_stack.append(token)
            elif token == '(':
                # Push opening parenthesis onto op_stack
                op_stack.append(token)
            elif token == ')':
                # Pop operators from op_stack and build AST nodes until matching opening parenthesis is found
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
                # Pop opening parenthesis from op_stack
                op_stack.pop()
            else:
                # Push operand onto ast_stack
                ast_stack.append({
                    'type': 'Literal' if self.is_number(token) else 'Identifier',
                    'value': token
                })

        # Pop remaining operators from op_stack and build AST nodes
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

