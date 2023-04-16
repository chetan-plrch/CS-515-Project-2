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


def check_invalid_expr(type):
    # Cases that are handled:
    # ++x + ++y - Valid
    # x++ + y++ - Valid
    # ++x + y++ - Valid
    # x++ + ++y - Valid
    # ------ ------ ------
    # ++x+++y - Not a valid case
    # x+++y++ - Valid case
    # ++x+y++ - Valid case
    # x+++++y - Not a valid case

    types = ['POST_INCREMENT', 'POST_DECREMENT', 'INCREMENT', 'DECREMENT']
    combinations = []
    for t1 in types:
        for t2 in types:
            combinations.append(f'{t1}-{t2}')

    if type in combinations:
        raise Exception('Two consecutive ++ -- found!')


class Tokenizer:
    def __init__(self, text):
        self.tokens = []
        self.current_token = None
        self.pos = 0
        self.text = text
        self.token_map = [
            (r'^#(.)*$', 'SINGLELINE_COMMENT'),
            (r'/\*\*.+?\*/', 'MULTILINE_COMMENT'),
            (r'[ \t]+', None),
            (r'\n', 'NEWLINE'),
            (r'[A-Za-z][A-Za-z0-9_]*\+\+', 'POST_INCREMENT'),
            (r'[A-Za-z][A-Za-z0-9_]*\-\-', 'POST_DECREMENT'),
            (r'\+\+', 'PRE_INCREMENT'),
            (r'--', 'PRE_DECREMENT'),
            (r'\+', 'PLUS'),
            (r'-', 'MINUS'),
            (r'\*', 'MULTIPLY'),
            (r'/', 'DIVIDE'),
            (r'%', 'MODULO'),
            (r'\^', 'POWER'),
            (r'\(', 'LPAREN'),
            (r'\)', 'RPAREN'),
            (r'=', 'ASSIGN'),
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
                        self.tokens.append(( token.get_type(), token.get_value() ))
                    self.pos += len(match.group())
                    break
            else:
                raise SyntaxError(f"Invalid token at position {self.pos}")
        t = Token('EOF')
        self.tokens.append(( t.get_type(), t.get_value() ))
        return self.tokens

    def create_tokens(self):
        f = self.text
        line_tokens = []
        for line in f.splitlines():
            line_tokens.append(Tokenizer(line).tokenize())
        return line_tokens

    def char_with_type_tokenized_lines(self):
        line_tokens = self.create_tokens()
        token_values = []
        i = 0
        for tokens in line_tokens:
            token_values.append([])
            for t in tokens:
                ch = t[1]
                if not ((ch == '\n') or (ch == None)):
                    token_values[i].append(t)

            for j in range(0, len(token_values[i])):
                if j > 0:
                    prev_type = token_values[i][j - 1][0]
                    cur_type = token_values[i][j][0]
                    check_invalid_expr(f'{prev_type}-{cur_type}')
            i += 1
        return token_values

    def char_without_type_tokenized_lines(self):
        line_tokens = self.create_tokens()
        token_values = []
        i = 0
        for tokens in line_tokens:
            token_values.append([])
            for t in tokens:
                ch = t[1]
                if not ((ch == '\n') or (ch == None)):
                    token_values[i].append(ch)
            i += 1
        return token_values

    def char_without_type_tokenized_line(self, tokens):
        token_values = []
        i = 0
        for t in tokens:
            ch = t[1]
            if not ((ch == '\n') or (ch == None) or (ch == 'SINGLELINE_COMMENT') or (ch == 'MULTILINE_COMMENT')):
                token_values[i].append(ch)
        return token_values







