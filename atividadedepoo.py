notas = [] 
while True:
    valor = float(input("Digite uma nota (ou -1 para parar): "))
    if valor == -1:
        break
    notas.append(valor)
print("\nQuantidade de notas lidas:", len(notas))
print("\nNotas na ordem informada:")
for n in notas:
    print(n, end=" ")
print("\n\nNotas na ordem inversa:")
for n in reversed(notas):
    print(n)
soma = sum(notas)
print("\nSoma das notas:", soma)

media = soma / len(notas)
print("Média das notas:", media)

acima_media = 0
for n in notas:
    if n > media:
        acima_media += 1
print("Quantidade de notas acima da média:", acima_media)
abaixo_sete = 0
for n in notas:
    if n < 7:
        abaixo_sete += 1
print("Quantidade de notas abaixo de 7:", abaixo_sete)
print("\ncabousse!")
