# (c) Georgii Semenov / MrGeorgeous 2021
# Декодер текста

import sys
if len(sys.argv) < 2:
    print("Specify the filename as command line argument.")
    exit(1)

fn = sys.argv[1]

decode = True
if len(sys.argv) >= 3:
    if sys.argv[2] == "--encode":
        decode = False

d = dict()
d['0'] = 'а'
d['1'] = 'б'
d['2'] = 'в'
d['3'] = 'г'
d['4'] = 'д'
d['5'] = 'е'
d['6'] = 'ж'
d['7'] = 'з'
d['8'] = 'и'
d['9'] = 'й'
d[':'] = 'к'
d[';'] = 'л'
d['<'] = 'м'
d['='] = 'н'
d['>'] = 'о'
d['?'] = 'п'
d['@'] = 'р'
d['A'] = 'с'
d['B'] = 'т'
d['C'] = 'у'
d['D'] = 'ф'
d['E'] = 'х'
d['F'] = 'ц'
d['G'] = 'ч'
d['H'] = 'ш'
d['I'] = 'щ'
d['J'] = 'ъ'
d['K'] = 'ы'
d['L'] = 'ь'
d['M'] = 'э'
d['N'] = 'ю'
d['O'] = 'я'

if decode is False:
    dd = dict()
    for k in d:
        dd[d[k]] = k

    for i in range(ord('А'), ord('Я')):
        dd["" + chr(i)] = ''

    d = dd

with open(fn, encoding='utf-8') as f:
    s = f.read()
    if decode is True:
        pass
        #s = s.replace("  ", " ")

    for k in d:
        if k != '' :
            if decode is True:
                s = s.replace(" " + k, d[k])
            else:
                s = s.replace(k, " " + d[k])

    print(s)
    exit(0)

print("File could not be found or read.")
exit(1)