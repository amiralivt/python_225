import numpy as np
from io import StringIO

data = open('IR000407540.dly', encoding='utf-8')
data = np.genfromtxt('IR000407540.dly', delimiter=[11, 4, 2, 4, 248],
                     dtype="S11,i4,i2,S4,S248",
                     names=['ID', 'YEAR', 'MONTH', 'ELEMENT', 'VALUE'])

newData = []
f = open("data.csv", "w")
f.write("ID, YEAR, MONTH, DAY, ELEMENT, VALUE, MFLAG, QFLAG, SFLAG\n")

for row in data:
    values = data[0]['VALUE'].decode('utf8')
    dd = StringIO(values)
    dd.seek(0)
    ID = row['ID'].decode('utf8')
    YEAR = row['YEAR']
    MONTH = row['MONTH']
    ELEMENT = row['ELEMENT'].decode('utf8')
    for i in range(1, 32):
        VALUE = int(dd.read(5))
        MFLAG = dd.read(1)
        QFLAG = dd.read(1)
        SFLAG = dd.read(1)
        f.write(f"'{ID}', {YEAR}, {MONTH}, {i}, '{ELEMENT}', {VALUE}, '{MFLAG}', '{QFLAG}', '{SFLAG}' \n")

f.close()
