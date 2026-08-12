from stack import Stack

S = Stack()

S.push(10)
S.push(2)
print(f'S의 길이: {len(S)}\n')

print(f'S의 상단부 원소: {S.top()}\n')

S.pop()
print(f'pop을 수행한 후의 S 상단부 원소: {S.top()}')