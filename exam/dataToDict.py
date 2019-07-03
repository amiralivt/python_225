import numpy as np
from io import StringIO

data = open('IR000407540.dly', encoding='utf-8')
data = np.genfromtxt('IR000407540.dly', delimiter=[11, 4, 2, 4, 248],
                     dtype="S11,i4,i2,S4,S248",
                     names=['ID', 'YEAR', 'MONTH', 'ELEMENT', 'VALUE'])

newData = []

for row in data:
    # print(row)
    values = data[0]['VALUE'].decode('utf8')
    dd = StringIO(values)
    dd.seek(0)
    newValues = {}
    for i in range(1, 32):
        VALUE = dd.read(5)
        MFLAG = dd.read(1)
        QFLAG = dd.read(1)
        SFLAG = dd.read(1)
        newValues[i] = {"VALUE": int(VALUE), "MFLAG": MFLAG, "QFLAG": QFLAG, "SFLAG": SFLAG}

    newData.append(
        {"ID": row['ID'].decode('utf8'),
         "YEAR": row['YEAR'],
         "MONTH": row['MONTH'],
         "ELEMENT": row['ELEMENT'].decode('utf8'),
         "VALUES": newValues}
    )

print(newData)
