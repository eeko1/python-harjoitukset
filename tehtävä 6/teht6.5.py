
def kokoluku(lista):
    for i in lista:
        if i % 2 != 0:
            lukuja.remove(i)
    return lukuja

lukuja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lukuja)
print(kokoluku(lukuja))