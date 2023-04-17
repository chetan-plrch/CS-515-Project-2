import Printer
import Tokenizer
expressions = [
  "++a + b-- * c++ - d + ++e",
  "f-- * ++g - ++h * i-- + j",
  "--k + ++l * m-- + n * o--",
  "p-- * ++q * --r + s-- - ++t",
  "u + ++v - w-- * x++ * --y + z",
  "++aa * bb-- * cc + --dd - ee++ + ff",
  "++gg - hh-- * ii++ * jj - kk-- + ll",
  "--mm * ++nn + oo-- * pp + qq-- - ++rr",
  "ss * --tt + uu-- - vv++ * ++ww - xx",
  "++yy - zz-- * aaa * bbb-- - ccc + ++ddd",
  "eee-- + ++fff * --ggg * hhh - iii-- + jjj",
  "kkk * ++ll - mm * --nn + ooo-- - ++pp",
  "++qq * --rr * ss-- + ++tt - uu + vvv--",
  "www-- - ++xxx * yyy-- * ++zz - aaa * bbb++",
  "ccc + ++ddd * eee-- - fff-- * --ggg + ++hhh",
  "iii-- * ++jjj * --kkk + lll-- + ++mmm - nnn",
  "++ooo - ppp-- * qqq++ * --rrr - sss + ttt--",
  "uuu-- * ++vv - www-- * ++xxx + yyy - zzz++",
  "++aaa * bbb-- + --ccc * ddd-- - eee * ++fff",
  "ggg-- * ++hhh - iii-- + jjj-- * kk++ + ll * --mmm"
]

x = Printer.Printer()
x.assigner(f'x=1')
x.assigner(f'++x + ++y')
x.assigner(f'print x, y')

for i in range(len(expressions)):
    t = Tokenizer.Tokenizer(expressions[i])
    prgm = t.text
    lines = prgm.split('\n')

    # x = Printer.Printer()
    # x.assigner(f'x=1')
    # x.assigner(f'++x + ++y')
    # x.assigner(f'print x')
    # x.assigner(f'print y')

    # for line in lines:
    #   x = Printer.Printer()
    #   x.assigner(f'a={expressions[i]}')
    #   x.assigner(f'         print a      ')

