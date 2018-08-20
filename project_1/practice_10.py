from functools import reduce

def str2num(s):
    return int(s)  # method 1: change this line to 'return float(s)'

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')  # method 2: change 7.6 on this and next line to any integer
    print('99 + 88 + 7.6 =', r)

main()
