a, b = map(int, input().split())
# print(a, b)

product = a * b
# print(product)

if product % 2 == 1:
    print('Odd')
else:
    print('Even')
