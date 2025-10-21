
numeros = [10, 20, 30, 40, 50]
print("lista inicial:", numeros)
print("primeiro número:", numeros[0])
print("número do meio:", numeros[2])
print("ultimo número:", numeros[-1])
numeros[1] = 25
print("lista depois de modificar um número:", numeros)
novo_numero = int(input("digite um número para adicionar à lista: "))
numeros.append(novo_numero)
print("lista depois de adicionar o número:", numeros)
numeros.remove(30)
print("lista depois de remover um número:", numeros)
