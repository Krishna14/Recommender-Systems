import numpy as np

values = [i for i in range(2, 10)]

def return_values():
  idx = 0
  while(idx < len(values)):
    yield values[idx]
    idx += 1

j = 0
for val in return_values():
  while j in np.arange(1, val):
    print(j)
