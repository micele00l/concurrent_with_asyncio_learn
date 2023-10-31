import numpy as np
import time
data_point = 4000000000
rows = 50
columns = int(data_point/rows)

matrix = np.arange(data_point).reshape(row, columns)
s = time.time()
res = np.mean(matrix, axis=1)
e = time.time()
print(e-s)
