import io
import sys

_INPUT = """\
6
3 4
1 0
246 402
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  if A==0:
    print(0,1)
  else:
    x=1/((1+B**2/A**2)**.5)
    print(x,B/A*x)