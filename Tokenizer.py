import re


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __str__(self):
        return f'{self.type}, {self.value}'

    def value(self):
        return self.type, self.value

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value;


operator_types = {
    'INCREMENT': 'INCREMENT',
    'DECREMENT': 'DECREMENT',
    'PLUS': 'PLUS',
    'MINUS': 'MINUS',
    'MULTIPLY': 'MULTIPLY',
    'DIVIDE': 'DIVIDE',
    'MODULO': 'MODULO',
    'POWER': 'POWER',
    'LPAREN': 'LPAREN',
    'RPAREN': 'RPAREN'
}


operand_type = {
    'NAME': 'NAME',
    'NUMBER': 'NUMBER'
}


class Tokenizer:
    def __init__(self, text):
        self.tokens = []
        self.current_token = None
        self.pos = 0
        self.text = text
        self.token_map = [
            (r'[ \t]+', None),
            (r'\n', 'NEWLINE'),
            (r'\+\+', 'INCREMENT'),
            (r'--', 'DECREMENT'),
            (r'\+', 'PLUS'),
            (r'-', 'MINUS'),
            (r'\*', 'MULTIPLY'),
            (r'/', 'DIVIDE'),
            (r'%', 'MODULO'),
            (r'\^', 'POWER'),
            (r'\(', 'LPAREN'),
            (r'\)', 'RPAREN'),
            (r'=', 'ASSIGN'),
            (r'print', 'PRINT'),
            (r'[A-Za-z][A-Za-z0-9_]*', 'NAME'),
            (r'\d+(\.\d+)?', 'NUMBER'),
        ]

    def tokenize(self):
        while self.pos < len(self.text):
            for pattern, token_type in self.token_map:
                match = re.match(pattern, self.text[self.pos:])
                if match:
                    if token_type:
                        token = Token(token_type, match.group())
                        self.tokens.append((
                            token.get_type(),
                            token.get_value()
                        ))
                    self.pos += len(match.group())
                    break
            else:
                raise SyntaxError(f"Invalid token at position {self.pos}")
        t = Token('EOF')
        self.tokens.append(( t.get_type(), t.get_value() ))
        return self.tokens


def create_tokens():
    f = open('test_program.txt').read()
    t = Tokenizer(f)
    return t.tokenize()


values = {
    'x': 1,
    'y': 2,
    'z': 3,
    'z1': 4,
    'z2': 5,
    'xhksdjhfkjhsdfhk': 8,
    'z3': 6
}


def substitute_parse_values(token):
    type, value = token
    if type == 'NAME':
        return 'NUMBER', float(values[value])
    elif type == 'NUMBER':
        return 'NUMBER', float(value)
    return token


def evaluation(tokens):
    # Implement stack based parsing for evaluation
    pass


evaluation(create_tokens())


# How to evluate an

