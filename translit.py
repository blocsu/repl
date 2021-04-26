s = 'Доценко Евгений Владимирович'


def translit(s):
    cyrillic1 = ' абвгдеёжзийклмнопрстуф'
    cyrillic2 = 'хцчшщъыьэюяАБВГДЕЁЖЗИЙК'
    cyrillic3 = 'ЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin1 = ' |a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f'
    latin2 = '|kh|ts|ch|sh|shch|ie|y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K'
    latin3 = '|L|M|N|O|P|R|S|T|U|F|Kh|Ts|Ch|Sh|Shch|Ie|Y||E|Iu|Ia'
    cyrillic = cyrillic1 + cyrillic2 + cyrillic3
    latin = (latin1 + latin2 + latin3).split('|')
    d = dict(zip(cyrillic, latin))
    str = ''
    for i in range(len(s)):
        for key, value in d.items():
            if key == s[i]:
                str += value
    return str


print(translit(s))
