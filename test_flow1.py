import Printer

x=Printer.Printer()
x.assigner("x=1")
x.assigner("y=2")
print(x.assigner("y=++x + --y"))
# x.assigner("z=10+x")


# x.assigner("x=(4 + 2) * (3 - 5) / 2 % 3 ^ 2 ")