numeros=[]
for i in range(10):
    numeros=int(input(f"Digite o{i+1}° numero:"))
    numeros.append(numeros)
    tupla=tuple(numeros)
    print("Tupla na ordem inversa:")
    for numeros in reversed(tupla):
        print(elemento)
