# python3
# wszystkie numery telefonów i adresy e-mail z tekstu, który znajduje się w schowku

import re
import pyperclip

# wyszukiwanie numerów
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))                           # numer kierunkowy albo pierwsze trzy liczby
    (\s|-|\.)?                                  # separator
    (\d{3})                                     # trzy cyfry
    (\s|-|\.)?                                  # separator
    (\d{3,4})                                   # ostatnir trzy albo cztery cyfry
    (\s*(ext|x|ext.|wew|wew.)\s*(\d{2,5}))?     # numer wewnętrzny
    )''', re.VERBOSE)

# wyszukiwanie maili
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # nazwa użytwkownika
    @                       # znak 'at'
    [a-zA-Z0-9.-]+          # nazwa domeny
    (\.[a-zA-Z]{2,4})       # rodzaj domeny
    )''', re.VERBOSE)


# test of regular expressions
# text = "Ala ma kota, a kot ma Ale. Ala ma numer 404-203-502 wew 12. Kot ma email kotokalipsa@kotyn.pl. Co z tego wynika? Niewiadomo :("

# Wyszukiwanie dopasowań w tekście ze schowka
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# skopiowanie wyników do schowka
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('skopiowano do schowka:')
    print('\n'.join(matches))
else :
    print('nie znaleziono żadnego dopasowania')