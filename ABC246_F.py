import io
import sys

_INPUT = """\
6
2 2
ab
ac
4 3
abcdefg
hijklmnop
qrstuv
wxyz
5 1000000000
abc
acde
cefg
abcfh
dghi
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import combinations
  mod=998244353
  N,L=map(int,input().split())
  S=[set(list(input())) for i in range(N)]
  ans=0
  for i in range(N):
    for c in combinations(list(range(N)), i+1):
      s=S[c[0]]
      for j in range(i):
        s=s.intersection(S[c[j+1]])
      if i%2==0:
        ans=(ans+pow(len(s),L,mod))%mod
      else:
        ans=(ans-pow(len(s),L,mod))%mod
  print(ans)