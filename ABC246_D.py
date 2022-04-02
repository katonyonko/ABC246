import io
import sys

_INPUT = """\
6
9
0
999999999989449206
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=10**18
  for b in range(10**6+1):
    l,r=b-1,10**6
    while r-l>1:
      mid=(l+r)//2
      if mid**3+mid**2*b+mid*b**2+b**3>=N: r=mid
      else: l=mid
    ans=min(ans,r**3+r**2*b+r*b**2+b**3)
  print(ans)