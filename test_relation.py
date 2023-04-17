import Printer

x = Printer.Printer()
lister = ["(a < b) && (c >= d) && ((e != f) || (g == h))",  "(x != y) || (z >= w) && (p == q)",  "(m >= n) || ((p != q) && (r < s))",  "(a <= b) && (c > d) && (e > f) || (g != h)",  "(x > y) || (z == w) && (p < q)",
          "(a == b) || ((c != d) && (e <= f))",  "(x >= y) && (z < w) || ((p != q) && (r > s))",  "(m != n) && (p >= q) || (r < s)",  "(a < b) || ((c == d) && (e >= f))",  "(x <= y) && (z > w || p == q)"]

for index,i in enumerate(lister):
    print("Index",index)
    print(x.assigner("x="+i))

