import io
import sys

_INPUT = """\
6
-1 -1
-1 2
3 2
-60 -40
-60 -80
-20 -80
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  XY=[list(map(int,input().split())) for _ in range(3)]
  X=[XY[i][0] for i in range(3)]
  Y=[XY[i][1] for i in range(3)]
  for i in range(3):
    if X.count(X[i])==1:
      x=X[i]
    if Y.count(Y[i])==1:
      y=Y[i]
  print(x,y)