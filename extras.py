import re


def get_print_items(line):
    m = re.match(f'\s*print\s*(.*)', line)
    variables = m.group(1).split(',')
    variables = list(map(lambda variable: variable.strip(), variables))
    return variables

