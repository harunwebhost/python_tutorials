l = []
def enque(item):
    l.append(item)
enque(50)
enque(502)
enque(5028)

def deque():
    del(l[0])

deque()
deque()
print(l)
