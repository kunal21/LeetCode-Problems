import math
n = 16
if n == 0 or n < 0:
    print("False")
if 2**int(math.log(n)/math.log(2)) == n:
    print("True")
else:
    print("False")