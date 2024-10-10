# Definindo as funções para as operações
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return x / y

# Exibindo as opções para o usuário
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Coletando a escolha do usuário
escolha = input("Digite a opção (1/2/3/4): ")

# Coletando os números para realizar a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando a operação com base na escolha
if escolha == '1':
    print(f"O resultado da soma é: {soma(num1, num2)}")
elif escolha == '2':
    print(f"O resultado da subtração é: {subtracao(num1, num2)}")
elif escolha == '3':
    print(f"O resultado da multiplicação é: {multiplicacao(num1, num2)}")
elif escolha == '4':
    print(f"O resultado da divisão é: {divisao(num1, num2)}")
else:
    print("Opção inválida!")

