# Sem estruturas condicionais

valor_ano1 = float(input("Digite o valor do carro no primeiro ano: "))
valor_ano2 = float(input("Digite o valor do carro no segundo ano: "))
valor_ano3 = float(input("Digite o valor do carro no terceiro ano: "))

valor_mais_alto = max(valor_ano1, valor_ano2, valor_ano3)
valor_mais_baixo = min(valor_ano1, valor_ano2, valor_ano3)

print(f"O valor mais alto é: {valor_mais_alto}")
print(f"O valor mais baixo é: {valor_mais_baixo}")