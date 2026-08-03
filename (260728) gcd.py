def gcd(a, b):
    while a*b != 0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b


x, y = map(int, input('두 수를 입력하세요. (공백 한줄 입력): ').split())
print('x, y의 최대공약수: ', gcd(x, y))