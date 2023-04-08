import re

stmt_type = {
    'E': 'EXPRESSION',
    'A': 'ASSIGNMENT',
    'AV': 'ASSIGNMENT_VARIABLE',
    'AC': 'ASSIGNMENT_CONSTANT',
    'AE': 'ASSIGNMENT_EXPRESSION',
    'P': 'PRINT',
    'PE': 'PRINT_EXPRESSION',
    'CMT': 'COMMENT',
    'M_CMT': 'MULTILINE_COMMENT'
}

stmt1 = 'a = 23'
stmt2 = ''
stmt3 = ''

variable_regex = '[a-zA-Z_]\w*'
signed_variable_regex = '[+-]?[a-zA-Z_]\w*'
signed_constant_regex = '[+-]?[0-9]{1,}([.][0-9]{1,})?'
spaced_signed_variable_regex = f'\s*{signed_variable_regex}\s*'
spaced_signed_constant_regex = f'\s*{signed_constant_regex}\s*'

def is_variable(str):
    pass


def is_constant(str):
    pass


def is_expression(str):
    pass


def is_assignment_const(line):
    return bool(re.fullmatch(f'{variable_regex}={spaced_signed_constant_regex}$', line, re.IGNORECASE))


def is_assignment_variable(line):
    return bool(re.fullmatch(f'\s*{variable_regex}\s*=\s*{signed_variable_regex}\s*$', line, re.IGNORECASE))


def classify_stmt(line):
    print(is_assignment_variable(line))


line = 'a =   +kfhdh_dfsad'
classify_stmt(line)
# Rules for EXPRESSION statement
# 1. One or more Operator with one or more 'variable' / 'constant' / 'both'

# Rules for a ASSIGNMENT statement
# 1. Left hand should be a 'variable'
# 2. Operator after left hand should be '='
# 3. Right hand should be a 'variable' or 'constant'

# Rules for ASSIGNMENT_EXPRESSION statement
# 1. Left hand should be a 'variable'
# 2. Operator after left hand should be '='
# 3. Right hand should consist of operators

# Rules for PRINT statement
# 1. print followed by one or more 'constant' values or with one or more 'variable' values

# Rules for PRINT_EXPRESSION statement
# 1. print followed by an expression

# Rules for single-line COMMENT
# 1. Any line starting with '#' character

# Rules for multi-line - MULTILINE_COMMENT
# 1. Any set of lines starting with '/*' character and ending with '*/'
# 2. If there's no '*/' character at the end of any line than it is invalid
