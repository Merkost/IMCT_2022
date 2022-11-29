# n, m = map(int, input().split())
# arr = [list(map(int, input())) for i in range(n)]
# count1, count2 = 0, 0
# for i in range(n):
#     for j in range(m):
#         if i >= 1 and j >= 0: count1 = arr[i - 1][j]
#         if i >= 0 and j >= 1: count2 = arr[i][j - 1]
#         arr[i][j] += max(count1, count2)
#         count1, count2 = 0, 0
# print(arr[-1][-1])

# m = []
# n = int(input())
# [m.append((price - 0.5)/count) for count, price in [map(int, input().split()) for i in range(n)]]
# print(max(m))

a, b, c = sorted(map(int, input().split()))
impossible = False
v = 0
while not impossible:
    # abc is Possible if: a*a + b*b == c*c




check([a,b,c])



# n, m = map(int, input().split())
# weights = list(map(int, input().split()))
# prices = list(map(int, input().split()))
# weights.insert(0, 0)
# prices.insert(0, 0)
# A = []
# for i in range(n + 1):
#     A.append([0] * (m + 1))
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         A[i][j] = A[i - 1][j]
#         if j >= weights[i] and A[i - 1][j - weights[i]] + prices[i] > A[i][j]:
#             A[i][j] = A[i - 1][j - weights[i]] + prices[i]
#
# print(A[n][m])
