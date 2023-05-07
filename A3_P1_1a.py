from __future__ import annotations
from typing import List

import collections
import heapq
import math

from utils import timeout


@timeout(10)
def mazeQ1a(graph: List[List[int]], start: List[int], end: List[int]):
    m, n = len(graph), len(graph[0])
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[False for _ in range(n)] for _ in range(m)]
    Q = collections.deque([])
    min_time = math.inf
    Q.append([*start, 0])
    
    while Q:
        cur = Q.popleft()
        x, y, time = cur[0], cur[1], cur[2]
        if x == end[0] and y == end[1]:
            min_time = min(min_time, time)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny] == 1:
                continue
            
            visited[nx][ny] = True
            Q.append([nx, ny, time + 1])
    return min_time if min_time != math.inf else -1
