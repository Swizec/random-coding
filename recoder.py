#!/usr/bin/python
# coding=utf8

TRANSLATIONS = [
    (',Ne,', ',0,'),
    (',Da,', ',1,'),

    # pay rate
    (',do 7€/h,', ',1,'),
    (',7€/h do 10€/h,', ',2,'),
    (',10€/h do 13€/h,', ',2,'),
    (',13€/h do 16€/h,', ',3,'),
    (',16€/h do 20€/h,', ',4,'),
    (',20€/h do 25€/h,', ',5,'),
    (',25€/h do 30€/h,', ',5,'),
    (',30€/h do 40€/h,', ',5,'),
    (',40€/h do 50€/h,', ',5,'),
    (',50€/h do 60€/h,', ',6,'),
    (',60€/h do 70€/h,', ',6,'),
    (',70€/h do 80€/h,', ',6,'),
    (',80€/h do 90€/h,', ',7,'),
    (',90€/h do 100€/h,', ',7,'),
    (',nad 100€/h,', ',7,'),

    # pay type
    (',Studentska napotnica,', ',1,'),
    (',Avtorska pogodba,', ',2,'),
    (',Lastno podjetje,', ',3,'),
    (',Navadna placa,', ',4,'),

    # study time
    (',do 10h', ',1'),
    (',11-20h', ',2'),
    (',21-30h', ',3'),
    (',31-40h', ',4'),
    (',nad 50h', ',5')
]

def recode(line):
    if ',Ne,' in line:
        return None
    for fr, to in TRANSLATIONS:
        line = line.replace(fr, to)
    return line

if __name__ == '__main__':
    f = open('raw_data.csv')
    ff = open('data.csv', 'w')

    map(ff.write,
        filter(lambda l: l != None,
               map(recode, f)))

    ff.close()
    f.close()
