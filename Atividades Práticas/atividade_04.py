# 1 - Desenvolva uma calculadora que realize as quatro operações básicas (+, -, *, /) entre dois números.

# Regras:
#   - Solicitar ao usuário dois números e a operação.

#   - Repetir até que uma operação válida seja concluída.

#   - Tratar os seguintes erros:

#   - Entrada não numérica.

#   - Divisão por zero.

#   - Operação inválida.

#   - Mostrar o resultado e encerrar.

# 2 - Crie um programa para o professor registrar as notas da turma.

# Regras:

#   - Continuar solicitando notas até que o professor digite 'fim'.

#   - Aceitar apenas notas entre 0 e 10.

#   - Ignorar notas inválidas e continuar solicitando.

#   - Ao final, mostrar a média da turma.

# 3 - Crie um programa que verifique se a senha é forte.

# Regras:

#   - Senha forte: pelo menos 8 caracteres e pelo menos um número.

#   - Continuar pedindo senha até que uma válida seja inserida ou o usuário digite 'sair'.

# 4 - Crie um programa que solicite números inteiros ao usuário.

# Regras:

#   - Continuar pedindo números até que o usuário digite 'fim'.

#   - Informar se o número é par ou ímpar.

#   - Se não for um número inteiro, informar o erro e continuar.

#   - Ao final, mostrar a quantidade total de números pares e ímpares inseridos.

# 1 - Calculadora Simples
def calculadora_simples():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero.")
                    continue
                resultado = num1 / num2
            else:
                print("Erro: Operação inválida.")
                continue

            print(f"Resultado: {resultado}")
            break

        except ValueError:
            print("Erro: Entrada não numérica.")

# 2 - Registro de Notas da Turma
def registrar_notas_turma():
    notas = []
    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").lower()
        if entrada == "fim":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# 3 - Verificador de Senha Forte
def verificador_senha_forte():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == "sair":
            break
        if len(senha) >= 8 and any(char.isdigit() for char in senha):
            print("Senha forte.")
            break
        else:
            print("Senha fraca. A senha deve ter pelo menos 8 caracteres e pelo menos um número.")

# 4 - Verificador de Par ou Ímpar
def par_ou_impar():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").lower()
        if entrada == "fim":
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("Número par.")
                pares += 1
            else:
                print("Número ímpar.")
                impares += 1
        except ValueError:
            print("Erro: entrada inválida, digite um número inteiro.")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")


# Menu de opções
if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Calculadora Simples")
    print("2 - Registro de Notas da Turma")
    print("3 - Verificador de Senha Forte")
    print("4 - Verificador de Par ou Ímpar")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        calculadora_simples()
    elif opcao == "2":
        registrar_notas_turma()
    elif opcao == "3":
        verificador_senha_forte()
    elif opcao == "4":
        par_ou_impar()
    else:
        print("Opção inválida.")
