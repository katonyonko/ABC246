import io
import sys

_INPUT = """\
6
5 4 7
8 3 10 5 13
5 100 7
8 3 10 5 13
20 815 60
2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K,X=map(int,input().split())
  A=list(map(int,input().split()))
  A.sort(reverse=True)
  i=0
  while i<N and K>0:
    tmp=min(K,A[i]//X)
    A[i]-=tmp*X
    K-=tmp
    i+=1
  A.sort(reverse=True)
  i=0
  while i<N and K>0:
    A[i]=0
    K-=1
    i+=1
  print(sum(A))