from __future__ import annotations
from typing import List

import collections
import heapq
import math

from utils import timeout
import pprint


@timeout(5)
def mazeQ1b(graph: List[List[int]], start: List[int], end: List[int], F: int):
    m, n = len(graph), len(graph[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dp = [[[math.inf, math.inf] for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    res = topdown(graph, dp, visited, start, end, F, start[0], start[1], False)
    return res if res else -1
    
def topdown(graph, dp, visited, start, end, F, x, y, used_flash):
    m, n = len(graph), len(graph[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    if x < 0 or x >= m or y < 0 or y >= n:
        return None
    if x == end[0] and y == end[1]:
        return 0

    if dp[x][y][used_flash] != math.inf:
        return dp[x][y][used_flash]
    
    min_dist = math.inf
    if not used_flash: # Not used flash yet
        for move in range(1, F + 1):
            for d in range(4):
                nx = x + dx[d] * move
                ny = y + dy[d] * move
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] == 1:
                    continue
                visited[x][y] = True
                dist = topdown(graph, dp, visited, start, end, F, nx, ny, True)
                visited[x][y] = False
                if dist is None:
                    continue
                min_dist = min(min_dist, 1 + dist)       
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            visited[x][y] = True
            dist = topdown(graph, dp, visited, start, end, F, nx, ny, False)
            visited[x][y] = False
            if dist is None:
                continue
            min_dist = min(min_dist, 1 + dist)
    else: # Already used flash
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            visited[x][y] = True
            dist = topdown(graph, dp, visited, start, end, F, nx, ny, True)
            visited[x][y] = False
            if dist is None:
                continue
            min_dist = min(min_dist, 1 + dist)
    dp[x][y][used_flash] = min_dist if min_dist != math.inf else None
    return dp[x][y][used_flash]

res = mazeQ1b(
    [[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0]],
    [0,0],
    [5,5],
    4
)
    
    
print(res)