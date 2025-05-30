import re
from datetime import date

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    :param valor_conta: Valor total da conta (float)
    :param porcentagem_gorjeta: Porcentagem da gorjeta (ex: 15 para 15%)
    :return: Valor da gorjeta calculada (float)
    """
    return valor_conta * (porcentagem_gorjeta / 100)


def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    :param texto: Palavra ou frase a ser verificada
    :return: "Sim" se for palíndromo, "Não" caso contrário
    """
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.

    :param ano_nascimento: Ano de nascimento (ex: 1990)
    :return: Idade estimada em dias
    """
    ano_atual = date.today().year
    idade_em_anos = ano_atual - ano_nascimento
    return idade_em_anos * 365

# 1. Gorjeta
print(calcular_gorjeta(100.0, 15)) 

# 2. Palíndromo
print(eh_palindromo("Ame a ema"))

# 3. Idade em dias
print(calcular_idade_em_dias(2000))
