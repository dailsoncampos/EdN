# 1 - Conversor de Moeda
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

print("=== Conversor de Moeda ===")
print(f"Valor em reais: R$ {valor_em_reais:.2f}")
print(f"Valor em dólares: US$ {valor_em_dolar:.2f}")
print(f"Valor em euros: € {valor_em_euro:.2f}")
print()

# 2 - Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("=== Calculadora de Desconto ===")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R$ {preco_final:.2f}")
print()

# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("=== Calculadora de Média Escolar ===")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")
print()

# 4 - Calculadora de Consumo de Combustível
distancia_km = 300
combustivel_litros = 25

consumo_medio = distancia_km / combustivel_litros

print("=== Calculadora de Consumo de Combustível ===")
print(f"Distância percorrida: {distancia_km} km")
print(f"Combustível gasto: {combustivel_litros} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
