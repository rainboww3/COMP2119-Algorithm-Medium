from __future__ import annotations
from typing import List

import collections
import heapq
import math

from utils import timeout


@timeout(5)
def mazeQ1b(graph: List[List[int]], start: List[int], end: List[int], F: int):
    m, n = len(graph), len(graph[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = {
        (1, 0): 1, # down
        (0, 1): 2, # right
        (-1, 0): 3, # up
        (0, -1): 4 # left
    }
    visited = [[[False, 0] for _ in range(n)] for _ in range(m)]
    visited[start[0]][start[1]] = [True, F]
    Q = collections.deque([])
    min_time = math.inf
    # 1: down, 2: right, 3:up, 4:left
    Q.append([*start, 0, F, None])
    
    
    while Q:
        cur = Q.popleft()
        x, y, time, remaining_flash, flash_direction = cur
        if graph[x][y] == 1 and remaining_flash == 0: # Stuck in a wall
            continue
        if x == end[0] and y == end[1]:
            min_time = min(min_time, time)
            
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny][0] and visited[nx][ny][1] > remaining_flash - 1:
                continue
            print(f"({x},{y}) -> ({nx},{ny}) / {remaining_flash}, {time}")
            
            if graph[nx][ny] == 1 or graph[x][y] == 1:
                if remaining_flash == 0:
                    continue
                elif remaining_flash == F: # not used flash yet
                   visited[nx][ny] = [True, remaining_flash - 1]
                   Q.append([nx, ny, time + 1, remaining_flash - 1, direction[(dx[d], dy[d])]]) 
                else: # 1 ~ F - 1
                    if direction[(dx[d], dy[d])] != flash_direction: # no different flash direction allowed
                        continue
                    else:
                        visited[nx][ny] = [True, remaining_flash - 1]
                        Q.append([nx, ny, time, remaining_flash - 1, flash_direction])      
            else:
                visited[nx][ny] = [True, remaining_flash]
                Q.append([nx, ny, time + 1, remaining_flash, flash_direction])
    print(min_time)
    return min_time if min_time != math.inf else -1

mazeQ1b(
    [[0,1,1,0],[0,0,1,0],[0,0,0,0],[0,1,1,0]],
    [0,0],
    [3,3],
    2
)