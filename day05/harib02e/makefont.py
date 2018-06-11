# encoding:utf-8


def convertFont(l):
    s = 0
    i = 0
    for b in l:
        if b == '*':
            s += 1 << (7 - i)
        i += 1
    return format(s, '#x')


c = open('hankaku.c', 'w')
t = open('hankaku.txt', 'r').read()
a = len(t.split('\n\n'))
a = str(a * 16)
s = 'char hankaku[%s] = {' % a

t = open('hankaku.txt', 'r')
i = 0

for l in t:
    if i % 18 >= 2:
        s += convertFont(l) + ', '
    i += 1
s = s.rstrip(', ')
s += '};'
c.write(s)
