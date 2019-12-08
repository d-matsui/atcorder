a = int(input())
b = int(input())
c = int(input())
x = int(input())
# print(a, b, c, x)

ans = 0
for i_a in range(0, a+1):
    for i_b in range(0, b+1):
        for i_c in range(0, c+1):
            sum = 500 * i_a + 100 * i_b + 50 * i_c
            if sum == x:
                ans += 1

print(ans)
