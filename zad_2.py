from wdi import *

def selection(n):
    print("Wybierz liczby do posortowania:")
    L = Array(n)
    for e in range(n):
        L[e] = int(input())

    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if L[j] < L[minimum]:
                minimum = j
        temp = L[i]
        L[i] = L[minimum]
        L[minimum] = temp
        
    for j in range(n):
        print(L[j], end=', ')


selection(5)

