import io
import sys

_INPUT = """\
6
5
1 3
3 5
....#
...#.
.....
.#...
#....
4
3 2
4 2
....
....
....
....
18
18 1
1 18
..................
.####.............
.#..#..####.......
.####..#..#..####.
.#..#..###...#....
.#..#..#..#..#....
.......####..#....
.............####.
..................
..................
.####.............
....#..#..#.......
.####..#..#..####.
.#.....####..#....
.####.....#..####.
..........#..#..#.
.............####.
..................
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs01(s):
    inf=10**10
    dist = [inf]*(N**2*4)
    que = deque()
    for i in s:
      dist[i] = 1
      que.append(i)
    dd=[[1,1],[1,-1],[-1,1],[-1,-1]]
    while que:
      q = que.popleft()
      i,j,d=q//(N*4), (q%(N*4))//4, (q%(N*4))%4
      for k in range(4):
        if d==k: continue
        ddd=dist[q] + 1
        if ddd<dist[i*N*4+j*4+k]:
          dist[i*N*4+j*4+k]=ddd
          que.append(i*N*4+j*4+k)
      ii, jj=i+dd[d][0], j+dd[d][1]
      if 0<=ii<N and 0<=jj<N and S[ii][jj]=='.' and dist[q]<dist[ii*N*4+jj*4+d]:
        dist[ii*N*4+jj*4+d]=dist[q]
        que.appendleft(ii*N*4+jj*4+d)
    return dist
  N=int(input())
  ax,ay=map(int,input().split())
  bx,by=map(int,input().split())
  ax-=1; ay-=1; bx-=1; by-=1
  S=[input() for _ in range(N)]
  dist=bfs01([ax*N*4+ay*4+i for i in range(4)])
  ans=min([dist[bx*N*4+by*4+i] for i in range(4)])
  if ans==10**10: print(-1)
  else: print(ans)