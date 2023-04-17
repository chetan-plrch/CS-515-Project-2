import re
import Printer

def get_print_items(line):
    m = re.match(f'\s*print\s*(.*)', line)
    variables = m.group(1).split(',')
    variables = list(map(lambda variable: variable.strip(), variables))
    return variables

# variable value

import re

def inbuilt_parser(token):
    # validate token
    variables = re.findall('\((.*)\)', token)[0].split(',')
    variables = list(map(lambda v: v.strip(), variables))
    return variables

print(inbuilt_parser('min(d , a)'))
expressions = [
  "(5 - 3) * (2 + 6) / 4 ^ 2 % 3",
  "((7 + 2) * 5) % 6 + 2 ^ 2 ^ 2",
  "(12 / 3) - (3 + 5) * (6 % 4) * 2",
  "10 * (8 - 2) / (5 + 3) ^ 2 % 2",
  "((6 + 4) / 2) ^ (9 % 5) - (3 * 2)",
  "8 + 6 / (4 * 2) - 1 % 3 ^ 2",
  "(5 * 3) + (9 - 2) / 4 ^ 2 - 6 % 2",
  "((11 - 3) / 2) ^ (8 % 5) + (7 * 2) / 3",
  "(6 + 2) * (8 / 4) ^ 2 % 5 - 1",
  "(3 * 5) - ((7 + 2) % 6) ^ 2 + 1 / 2",
  "7 ^ (8 % 3) * (5 - 3) + 1 / 2 - 4 * 3",
  "(9 + 2) * 3 - (7 / 2) % 4 ^ 2",
  "6 - (5 * 2) / (4 + 1) ^ 2 % 3 ^ 2",
  "((8 / 2) ^ 2) * (4 % 3) - (5 + 1)",
  "(3 + 4) * (7 - 2) / 6 ^ 2 % 2",
  "(6 * 5) - (7 % 3) ^ 2 + (9 / 3)",
  "(2 ^ 3) * (5 - 2) + 9 / (7 % 3) - 1",
  "(3 - 1) ^ 3 + (8 / 2) % 4 * 2",
  "5 + (6 * 3) - (7 - 2) / 4 ^ 2",
  "((8 / 2) * 4) % 7 + 1 ^ 3",
  "(5 * 2) - (10 % 3) ^ 2 / 4 + 1",
  "(4 + 2) * (3 - 5) / 2 % 3 ^ 2"
]



x = 1
y = 2
y = ++x + --y

y = x++ + y++ + ++x - ++y