N = int(input())
A = list(map(int, input().split()))
# print(N, A)

def check_all_even(A):
    # check if all numbers in A are even number
    for a in A:
        if a % 2 == 0:
            if a == A[-1]:
                return True
        else:
            return False

# print(check_all_even(A))

count = 0
while True:
    if check_all_even(A):
        count+=1
        A = list(map(lambda a: a / 2, A))
        # print(A)
    else:
        break

print(count)
