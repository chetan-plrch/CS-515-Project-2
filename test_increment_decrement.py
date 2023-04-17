import Printer
expressions = [
  "++a + b-- * c++ - d + ++e",
  "f-- * ++g - ++h / i-- + j",
  "--k + ++l * m-- + n / o--",
  "p-- * ++q / --r + s-- - ++t",
  "u + ++v - w-- * x++ / --y + z",
  "++aa * bb-- / cc + --dd - ee++ + ff",
  "++gg - hh-- / ii++ * jj - kk-- + ll",
  "--mm * ++nn + oo-- / pp + qq-- - ++rr",
  "ss / --tt + uu-- - vv++ * ++ww - xx",
  "++yy - zz-- / aaa * bbb-- - ccc + ++ddd",
  "eee-- + ++fff * --ggg / hhh - iii-- + jjj",
  "kkk * ++ll - mm / --nn + ooo-- - ++pp",
  "++qq / --rr * ss-- + ++tt - uu + vvv--",
  "www-- - ++xxx / yyy-- * ++zz - aaa / bbb++",
  "ccc + ++ddd / eee-- - fff-- * --ggg + ++hhh",
  "iii-- * ++jjj / --kkk + lll-- + ++mmm - nnn",
  "++ooo - ppp-- / qqq++ * --rrr - sss + ttt--",
  "uuu-- / ++vv - www-- * ++xxx + yyy - zzz++",
  "++aaa * bbb-- + --ccc / ddd-- - eee * ++fff",
  "ggg-- / ++hhh - iii-- + jjj-- * kk++ + ll / --mmm"
]

for i in range(len(expressions)):
    x=Printer.Printer()
    # print(expressions[i])
    try:
      print(expressions[i])
      print(x.assigner("x="+expressions[i]))
    except ZeroDivisionError:
       pass

  
