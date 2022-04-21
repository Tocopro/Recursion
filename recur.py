# recursive function

def calling_self(a, b):
    count = a
    for i in range(b + 1):
        count = count + i
    print(count)


calling_self(0, 10)
