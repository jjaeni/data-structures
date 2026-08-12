from dequeue import Dequeue

def check_palindrom(s):
    dq = Dequeue(s)
    palindrom = True

    while len(dq)>1:
         if dq.popleft() != dq.pop():
            palindrom = False
    return palindrom

s = input()
print(check_palindrom(s))