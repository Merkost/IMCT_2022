# import math
# import sys
#
# for i in sys.stdin.readlines():
#     print(math.isqrt(int(i)))
import numpy as np

countRows, countColumns = [int(i) for i in input().split()]
matrix = np.array([np.array(input().split()) for _ in range(countRows)])
print("\n".join(*matrix.transpose()))

