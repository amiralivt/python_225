import numpy as np

# data = open('IR000407540.dly')
# print()
data = np.genfromtxt('IR000407540.dly', delimiter=[11, 4, 2], dtype="S11,i4,i2",
                     names=['ID', 'YEAR', 'MONTH'])
print(data[0]['ID'].decode('utf-8'))
