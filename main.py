#62
def dict_len(d):
    return len(d)

print(dict_len({"a":1,"b":2,"c":3}))

#63
def qiymatlar(d):
    return list(d.values())

print(qiymatlar({"a":1,"b":2}))

#64
def juft_index(lst):
    return lst[::2]

print(juft_index([10,20,30,40,50]))

#65
def toq_index(lst):
    return lst[1::2]

print(toq_index([10,20,30,40,50]))

#66
def takror(text,n):
    for _ in range(n):
        print(text)

takror("salom",3)
