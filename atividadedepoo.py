while True:
    nome = input("Digite seu nome: ").strip()
    if not nome or nome.isdigit():
        print("Erro: o nome não pode ser vazio e nem conter números. Tente denovo.\n")
        continue
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: a idade deve ser um número inteiro. Tente denovo.\n")
        continue
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")
    break