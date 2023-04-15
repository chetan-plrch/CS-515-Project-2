import Printer

x=Printer.Printer()
x.token_helper_pre_post(
# [('NAME', 'x'), ('PLUS', '+'), ('LPAREN', '('), ('PRE_INCREMENT', '++'), ('NAME', 'y'), ('RPAREN', ')')]
# [('NAME', 'x'), ('MINUS', '-'), ('MINUS', '-'), ('NAME', 'y')]
# [('NAME', 'x'), ('PLUS', '+'), ('MINUS', '-'), ('NAME', 'y')]
[('NUMBER', '2'), ('MULTIPLY', '*'), ('MINUS', '-'), ('LPAREN', '('), ('NAME', 'x'), ('PLUS', '+'), ('NAME', 'y'), ('RPAREN', ')')]
)