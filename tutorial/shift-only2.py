N = int(input())
A = list(map(int, input().split()))

def how_many_times_divisible(n):
    times = 0
    while n % 2 == 0:
        times += 1
        n /= 2
    return times

ans = min(list(map(how_many_times_divisible, A)))
print(ans)
