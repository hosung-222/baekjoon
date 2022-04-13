#마인크래프트

from collections import Counter

def make_land(h):
    sec= 0
    for key in land:
        if key < h:
            sec += (h-key) *land[key]
            




















# import sys

# n, m, b = map(int,sys.stdin.readline().split())

# land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# h = 0
# ans = 1000000000000000000000000000000

# for i in range(257):
#     max = 0
#     min = 0

#     for j in range(n):
#         for k in range(m):
#             if land[j][k] < i:
#                 min += (i-land[j][k])
#             else:
#                 max += (land[j][k]-i)
#     inven = b + max
#     if inven < min:
#         continue
#     time = 2 * max + min
#     if time <= ans:
#         ans = time
#         h = i

# print(ans, h)


