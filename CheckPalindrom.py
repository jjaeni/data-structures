from DequeueAlgorithm import Dequeue

def check_palindrom(s):
    dq = Dequeue(s)
    palindrom = True

    while len(dq)>1:
        print(dq.left(), dq.right())
        if dq.left() != dq.right():
            palindrom = False

        dq.popleft()
        dq.pop()
        print(len(dq))
    return palindrom

s = input('문자열 입력하세요')
print(check_palindrom(s))