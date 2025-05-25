# Atividade Prática 03 - Estruturas de Controle

# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

# 1- Classificador de Idade

def classificador_idade():
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    else:
        print("Classificação: Idoso")

# 2- Calculadora de IMC
def calculadora_imc():
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obeso")
    except ZeroDivisionError:
        print("Altura inválida.")
    except ValueError:
        print("Entrada inválida.")

#3- Conversor de Temperatura
def conversor_temperatura():
    temp = float(input("Digite a temperatura: "))
    origem = input("Unidade de origem (C/F/K): ").upper()
    destino = input("Unidade de destino (C/F/K): ").upper()

    def celsius_para_fahrenheit(c): return c * 9/5 + 32
    def celsius_para_kelvin(c): return c + 273.15
    def fahrenheit_para_celsius(f): return (f - 32) * 5/9
    def fahrenheit_para_kelvin(f): return (f - 32) * 5/9 + 273.15
    def kelvin_para_celsius(k): return k - 273.15
    def kelvin_para_fahrenheit(k): return (k - 273.15) * 9/5 + 32

    if origem == destino:
        print(f"Temperatura convertida: {temp:.2f} {destino}")
        return

    try:
        if origem == "C":
            if destino == "F":
                print(f"Temperatura convertida: {celsius_para_fahrenheit(temp):.2f} F")
            elif destino == "K":
                print(f"Temperatura convertida: {celsius_para_kelvin(temp):.2f} K")
        elif origem == "F":
            if destino == "C":
                print(f"Temperatura convertida: {fahrenheit_para_celsius(temp):.2f} C")
            elif destino == "K":
                print(f"Temperatura convertida: {fahrenheit_para_kelvin(temp):.2f} K")
        elif origem == "K":
            if destino == "C":
                print(f"Temperatura convertida: {kelvin_para_celsius(temp):.2f} C")
            elif destino == "F":
                print(f"Temperatura convertida: {kelvin_para_fahrenheit(temp):.2f} F")
        else:
            print("Unidade inválida.")
    except:
        print("Erro na conversão.")

# 4- Verificador de Ano Bissexto
def verificador_ano_bissexto():
    ano = int(input("Digite o ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")


# Menu de opções
if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Classificador de Idade")
    print("2 - Calculadora de IMC")
    print("3 - Conversor de Temperatura")
    print("4 - Verificador de Ano Bissexto")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        classificador_idade()
    elif opcao == "2":
        calculadora_imc()
    elif opcao == "3":
        conversor_temperatura()
    elif opcao == "4":
        verificador_ano_bissexto()
    else:
        print("Opção inválida.")
