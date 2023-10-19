quantidades = input('quantas pessoas irar se hospedar: ')
if not quantidades.isnumeric():
        print('Digite apenas numeros !!!')
else:
    quantidades = int(quantidades)
    quarto = []
for quantidade in  range (quantidades):
    nome = input('nome: ')
    cpf = input('CPF: ')
    if not cpf.isnumeric():
        print('Digite apenas numeros para o cpf!!!')
    else:
        hospede = [nome, cpf]
        quarto.append(hospede)
        print(quarto)