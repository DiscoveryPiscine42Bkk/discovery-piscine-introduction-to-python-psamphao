from binascii import Error

from torch import t


value = int(input())
if value >= 25:
    print(Error)
else:
  for num in range(value,25):
         print("Inside the loop,my variadle is {num}")